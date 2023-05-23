from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/listfieldactivities", tags=["ListFieldActivities"])


@router.get("/all/", response_model=List[schema.GetListFieldActivities], status_code=200)
def get_all_listfieldactivities():
    return models.ListFieldActivities.get_all()

@router.get("/paginate/", response_model=List[schema.GetListFieldActivities], status_code=200)
def get_paginate_listfieldactivities_by_page_per_page(page:int, per_page: int):
    return models.ListFieldActivities.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetListFieldActivities, status_code=200)
def get_listfieldactivities_by_uuid(uuid: UUID4):
    return models.ListFieldActivities.get(uuid)

@router.post("/", response_model=schema.GetListFieldActivities, status_code=201)
def create_new_listfieldactivities(
    json_data: schema.PostListFieldActivities,
):
    data = models.ListFieldActivities(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetListFieldActivities, status_code=200)
def update_listfieldactivities_by_uuid(uuid: UUID4, json_data: schema.PutListFieldActivities):
    return models.ListFieldActivities.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_listfieldactivities_by_uuid(uuid: UUID4):
    return models.ListFieldActivities.remove(uuid)

    