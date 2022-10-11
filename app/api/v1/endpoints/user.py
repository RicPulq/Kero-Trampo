from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List
from ....core.security import *

from app import schema, models

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
    data = models.User(**json_data.dict())
    # hashing funcionou
    # data.password = get_password_hash(data.password)
    return data.create()


@router.put("/uuid", response_model=schema.GetUser, status_code=200)
def update_user_by_uuid(uuid: UUID4, json_data: schema.PutUser):
    return models.User.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_user_by_uuid(uuid: UUID4):
    return models.User.remove(uuid)
