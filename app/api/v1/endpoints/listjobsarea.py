from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/listjobsarea", tags=["ListJobsArea"])


@router.get("/all/", response_model=List[schema.GetListJobsArea], status_code=200)
def get_all_listjobsarea():
    return models.ListJobsArea.get_all()

@router.get("/paginate/", response_model=List[schema.GetListJobsArea], status_code=200)
def get_paginate_listjobsarea_by_page_per_page(page:int, per_page: int):
    return models.ListJobsArea.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.ShowList, status_code=200)
def get_listjobsarea_by_uuid(uuid: UUID4):
    return models.ListJobsArea.get(uuid)

@router.post("/", response_model=schema.GetListJobsArea, status_code=201)
def create_new_listjobsarea(
    json_data: List[schema.PostListJobsArea],
):
    _db = db.Session()
    for data_jobs in json_data:
        data = models.ListJobsArea(**data_jobs.dict())
        _db.add(data)
    _db.commit()
    return "OK"


@router.put("/uuid", response_model=schema.GetListJobsArea, status_code=200)
def update_listjobsarea_by_uuid(uuid: UUID4, json_data: schema.PutListJobsArea):
    return models.ListJobsArea.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_listjobsarea_by_uuid(uuid: UUID4):
    return models.ListJobsArea.remove(uuid)

    