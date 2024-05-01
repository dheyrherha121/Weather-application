from fastapi import APIRouter,Depends
from .. import schema,database,utility,model
from sqlalchemy.orm import session

router = APIRouter(
    prefix= '/users',
    tags= ['users']
)

@router.post('/', response_model=schema.UserOut)
def CreateUser(user: schema.User, db: session = Depends(database.get_db)):
    hash_password = utility.hash(user.password)
    user.password = hash_password
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
