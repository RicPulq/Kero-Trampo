from app import models, schema

from .user import admin
from .role import role

def pop_db():
    for data in role:
        role_schema = schema.Post
    user_schema = schema.PostUser(**admin)
    user = models.User(**user_schema.dict())
    user.create()
    

