from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/listpreviouslyjobs", tags=["ListPreviouslyJobs"])


@router.get("/all/", response_model=List[schema.GetListPreviouslyJobs], status_code=200)
def get_all_listpreviouslyjobs():
    return models.ListPreviouslyJobs.get_all()

@router.get("/paginate/", response_model=List[schema.GetListPreviouslyJobs], status_code=200)
def get_paginate_listpreviouslyjobs_by_page_per_page(page:int, per_page: int):
    return models.ListPreviouslyJobs.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetListPreviouslyJobs, status_code=200)
def get_listpreviouslyjobs_by_uuid(uuid: UUID4):
    return models.ListPreviouslyJobs.get(uuid)

@router.post("/", response_model=schema.GetListPreviouslyJobs, status_code=201)
def create_new_listpreviouslyjobs(
    json_data: schema.PostListPreviouslyJobs,
):
    data = models.ListPreviouslyJobs(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetListPreviouslyJobs, status_code=200)
def update_listpreviouslyjobs_by_uuid(uuid: UUID4, json_data: schema.PutListPreviouslyJobs):
    return models.ListPreviouslyJobs.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_listpreviouslyjobs_by_uuid(uuid: UUID4):
    return models.ListPreviouslyJobs.remove(uuid)

    