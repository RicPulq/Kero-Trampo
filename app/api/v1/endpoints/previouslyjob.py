from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/previouslyjob", tags=["PreviouslyJob"])


@router.get("/all/", response_model=List[schema.GetPreviouslyJob], status_code=200)
def get_all_previouslyjob():
    return models.PreviouslyJob.get_all()

@router.get("/paginate/", response_model=List[schema.GetPreviouslyJob], status_code=200)
def get_paginate_previouslyjob_by_page_per_page(page:int, per_page: int):
    return models.PreviouslyJob.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetPreviouslyJob, status_code=200)
def get_previouslyjob_by_uuid(uuid: UUID4):
    return models.PreviouslyJob.get(uuid)

@router.post("/", response_model=schema.GetPreviouslyJob, status_code=201)
def create_new_previouslyjob(
    json_data: schema.PostPreviouslyJob,
):
    data = models.PreviouslyJob(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetPreviouslyJob, status_code=200)
def update_previouslyjob_by_uuid(uuid: UUID4, json_data: schema.PutPreviouslyJob):
    return models.PreviouslyJob.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_previouslyjob_by_uuid(uuid: UUID4):
    return models.PreviouslyJob.remove(uuid)

    