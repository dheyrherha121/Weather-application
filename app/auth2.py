from jose import JWTError, jwt
from .config import setting
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from . import schema
from typing import Annotated
from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import session
from . import database, model



oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = setting.secret_key
ACCES_TOKEN_EXPIRE_MINUTES = setting.access_token_expire_minutes
ALGORITHM = setting.algorithm

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verifyaccesToken(token:str, credential_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id: str = payload.get('user_id')
        if id == None:
            raise credential_exception
        token_data = schema.TokenData(id = id)
    except JWTError:
        raise credential_exception
    return token_data

def get_curent_user(token:Annotated[str,Depends(oauth2_schema)], db: session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = verifyaccesToken(token, credential_exception)
    user = db.query(model.User).filter(model.User.id == token.id).first()
    return user