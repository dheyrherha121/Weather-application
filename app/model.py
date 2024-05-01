from .database import Base
from sqlalchemy import Column,Integer,String, TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = 'users'

    email= Column(String, nullable=False, unique=True)
    password= Column(String, nullable= False)
    id= Column(Integer, primary_key=True,nullable=False)
    created_now = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))