from app import models, schema

from .user import admin
from .role import role

def pop_db_init():
    for role_aux in role:
        print(role_aux["name"])
        if not models.Role.query_com_dois_params("name",role_aux["name"],None,None):
            role_schema = schema.PostRole
            role_schema = dict(role_aux)
            print(role_schema)
            roles = models.Role(**role_schema)
            roles.flush()
    print(admin)
    if not models.User.query_com_dois_params("username",admin["username"],None,None):
        user_schema = schema.PostUser(**admin)
        print(admin)
        user = models.User(**user_schema.dict())
        user.flush()
    
def pop_db():
    pass

