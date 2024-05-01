from fastapi import APIRouter, Depends,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import session
from ..database import get_db
from .. import model,utility,auth2
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix= '/login',
    tags= ['login']
)

@router.post('/')
def login(user_credential:Annotated[OAuth2PasswordRequestForm,Depends()], db: session= Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == user_credential.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='users not found')
    if not utility.verify(user_credential.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='incorrect credentials')
    access_token = auth2.create_token(data = {'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'Bearer'}
