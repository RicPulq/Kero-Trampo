from fastapi import APIRouter, Depends, HTTPException, Query, Header
import random, string
from ....core.security import get_password_hash, verify_password

from app import schema, models, db, auth, core

import app.util as util

router = APIRouter(tags=["Login"])


@router.post("/login/", response_model=schema.LoginResponse)
# @router.post("/login/", status_code=200)
def login(login: schema.Login):
    """Logar"""
    # print(login.username, login.password)
    user = models.User.login(username=login.username, password=login.password)
    sub = {"user_uuid": str(user.uuid), "key": [user.role.permission_level]}
    if user.role.name == "admin" and user.role.permission_level == 5:
        for i in range(1, user.role.permission_level):
            sub["key"].append(i)

    response = schema.LoginResponse(
        token=auth.encode_token(
            sub,
            core.settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
        user=user.username,
    )

    return response


@router.post("/forgot_password", status_code=200)
def forget_password(email: str):
    try:
        if models.User.exist("username",email):
            uuid = str(models.User.exist("username",email).uuid)
            letters = string.ascii_uppercase
            digits = string.digits
            aux = []
            for i in range(10):
                aux.append(random.choice(digits))
                aux.append(random.choice(letters))
            aux = random.sample(aux, 6)
            aux2 = "".join(aux)
            aux3 = get_password_hash(aux2)
            print(aux2)
            sub = {"uuid": uuid, "chave": aux3}
            reponse = schema.LoginResponse(
                token=auth.encode_token(
                    sub,
                    core.settings.ACCESS_TOKEN_EXPIRE_MINUTES,
                ),
                user=sub["uuid"],
            )
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=f"Usuário não encontrado.")
    return reponse, util.send_reset_password_email(email, aux2)


@router.put("/reset_password", status_code=200)
def reset_password( json_data: schema.PutUser, forgot_token: str = Header(..., description="Código token com o código de verificação"), code: str = Query(description="Código de verificação",max_length=6)):
    """Só atualizar a senha nessa rota"""
    try:
        aux = auth.decode_token(forgot_token)
        if verify_password(code, aux["chave"]):
            json_data.password = get_password_hash(json_data.password)
            return models.User.update(aux["uuid"], **json_data.dict(exclude_unset=True))
        raise HTTPException(status_code=401, detail=f"Acesso não autorizado.")
    except HTTPException as e:
        raise HTTPException(status_code=401, detail=f"Acesso não autorizado.")
    return "Ok"
