from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/address", tags=["Address"])


@router.get("/all/", response_model=List[schema.GetAddress], status_code=200)
def get_all_address():
    return models.Address.get_all()

@router.get("/paginate/", response_model=List[schema.GetAddress], status_code=200)
def get_paginate_address_by_page_per_page(page:int, per_page: int):
    return models.Address.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetAddress, status_code=200)
def get_address_by_uuid(uuid: UUID4):
    return models.Address.get(uuid)

@router.post("/", response_model=schema.GetAddress, status_code=201)
def create_new_address(
    json_data: schema.PostAddress,
):
    data = models.Address(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetAddress, status_code=200)
def update_address_by_uuid(uuid: UUID4, json_data: schema.PutAddress):
    return models.Address.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_address_by_uuid(uuid: UUID4):
    return models.Address.remove(uuid)

    