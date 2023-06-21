from uuid import UUID
from app import models, schema

from .user import admin
from .role import role
from ..core.security import get_password_hash

def pop_db_init():
    for role_aux in role:
    # percorre toda a lista de dados "role"
        if not models.Role.query_com_dois_params("name",role_aux["name"],None,None):
        # verifica no banco se já existe os dados, caso não cria no banco as "roles" 
            role_schema = schema.PostRole
            role_schema = dict(role_aux)
            roles = models.Role(**role_schema)
            roles.create()
    if not models.User.query_com_dois_params("username",admin["username"],None,None):
    # verifica no banco se já existe o usuário "admin" e caso não cria
        admin["password"] = get_password_hash(admin["password"])
        admin["active"] = True
        aux_role = role[0]
        data_role = models.Role.query_com_dois_params("name",aux_role["name"],"permission_level",aux_role["permission_level"])
        admin["role_uuid"] = data_role.uuid
        user_schema = schema.PostUser(**admin)
        user = models.User(**user_schema.dict())
        user.create()
    
def pop_db():
    pass

