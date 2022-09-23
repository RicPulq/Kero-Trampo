from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/role", tags=["Role"])


@router.get("/all/", response_model=List[schema.GetRole], status_code=200)
def get_all_role():
    return models.Role.get_all()

@router.get("/paginate/", response_model=List[schema.GetRole], status_code=200)
def get_paginate_role_by_page_per_page(page:int, per_page: int):
    return models.Role.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetRole, status_code=200)
def get_role_by_uuid(uuid: UUID4):
    return models.Role.get(uuid)

@router.post("/", response_model=schema.GetRole, status_code=201)
def create_new_role(
    json_data: schema.PostRole,
):
    data = models.Role(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetRole, status_code=200)
def update_role_by_uuid(uuid: UUID4, json_data: schema.PutRole):
    return models.Role.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_role_by_uuid(uuid: UUID4):
    return models.Role.remove(uuid)

    