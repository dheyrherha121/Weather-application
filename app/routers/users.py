from fastapi import APIRouter
from .. import schema

router = APIRouter(
    prefix= 'users',
    tags= ['users']
)

@router.post('/', response_model=schema.UserOut)
def CreateUser(user: schema.User):