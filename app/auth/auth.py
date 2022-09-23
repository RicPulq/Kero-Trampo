import datetime
from typing import Optional
from fastapi import Header, HTTPException
import jwt

from app import core, models


def encode_token(sub, exp):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=exp),
            "iat": datetime.datetime.utcnow(),
            "sub": sub,
        }
        result = (
            f"Bearer {jwt.encode(payload, core.settings.SECRET_KEY, algorithm='HS256')}"
        )
        return result
    except:
        raise HTTPException(status_code=400, detail=[{"msg": "Erro ao gerar Token!"}])


def decode_token(Autentication, key: Optional[int] = None):
    try:
        if not Autentication or not "Bearer" in Autentication:
            raise HTTPException(
                status_code=401,
                detail="Desculpe Você nao tem Permissão, Chave de acesso Invalida",
            )
        token = Autentication.split(sep=" ")
        payload = jwt.decode(token[1], core.settings.SECRET_KEY, algorithms="HS256")

        if "user_uuid" in payload["sub"]:
            if key not in payload["sub"]["key"]:
                raise HTTPException(
                    status_code=401,
                    detail=[{f"msg": "Desculpe Você nao tem Permissão Nivel {key}."}],
                )
            user = models.User.get(payload["sub"]["user_uuid"])
            if not user:
                raise HTTPException(
                    status_code=401,
                    detail=[
                        {
                            "msg": "Desculpe Você nao tem Permissão, Usuario Nao encontrado!"
                        }
                    ],
                )
            if not user.active:
                raise HTTPException(
                    status_code=401,
                    detail=[
                        {
                            "msg": "Desculpe Você nao tem Permissão, Usuario Desativado ou excluido!"
                        }
                    ],
                )
        return payload["sub"]

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail=[
                {"msg": "Desculpe Você nao tem Permissão, Chave de acesso expirada!"}
            ],
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail=[
                {"msg": "Desculpe Você nao tem Permissão, Chave de acesso Invalida!"}
            ],
        )


class Key:
    # vefifica se o usuario tem o nivel de permissao Maximo N5
    async def n5(Autentication: Optional[str] = Header(None)):
        payload = decode_token(Autentication, 5)
        return payload

    # vefifica se o usuario tem o nivel de permissao N4
    async def n4(Autentication: Optional[str] = Header(None)):
        payload = decode_token(Autentication, 4)
        return payload

    # vefifica se o usuario tem o nivel de permissao N3
    async def n3(Autentication: Optional[str] = Header(None)):
        payload = decode_token(Autentication, 3)
        return payload

    # vefifica se o usuario tem o nivel de permissao N2
    async def n2(Autentication: Optional[str] = Header(None)):
        payload = decode_token(Autentication, 2)
        if not models.User.exist("uuid", payload["user_uuid"]):
            raise HTTPException(
                status_code=401, detail=[{"msg": "Usuario nao encontrado"}]
            )
        return payload

    # vefifica se o usuario tem o nivel de permissao minima N1
    async def n1(Autentication: Optional[str] = Header(None)):
        payload = decode_token(Autentication)
        return payload
