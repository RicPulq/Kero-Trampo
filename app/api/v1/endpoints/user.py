from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List
from app.auth import auth
import app.util as util
import app.templates as templates

from ....core.security import *

from app import schema, models, core

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/all/", response_model=List[schema.GetUser], status_code=200)
def get_all_user():
    return models.User.get_all()


@router.get("/paginate/", response_model=List[schema.GetUser], status_code=200)
def get_paginate_user_by_page_per_page(page: int, per_page: int):
    return models.User.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowUser, status_code=200)
def get_user_by_uuid(uuid: UUID4):
    """Busca por UUID e tras tudo o que está relacionado"""
    return models.User.get(uuid)


@router.post("/", response_model=schema.GetUser, status_code=201)
def create_new_user(
    json_data: schema.PostUser,
):
    json_data.password = get_password_hash(json_data.password)
    data = models.User(**json_data.dict())
    
    return data.create(), util.send_email(json_data.username, core.settings.PROJECT_NAME, templates.conteudo)


@router.put("/uuid", response_model=schema.GetUser, status_code=200)
def update_user_by_uuid(uuid: UUID4, json_data: schema.PutUser, current_user = Depends(auth.Key.n1)):
    json_data.password = get_password_hash(json_data.password)
    return models.User.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_user_by_uuid(uuid: UUID4, current_user: str = Depends(auth.Key.n5)):
    return models.User.remove(uuid)
