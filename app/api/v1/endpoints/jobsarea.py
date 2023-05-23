from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/jobsarea", tags=["JobsArea"])


@router.get("/all/", response_model=List[schema.GetJobsArea], status_code=200)
def get_all_jobsarea():
    return models.JobsArea.get_all()

@router.get("/paginate/", response_model=List[schema.GetJobsArea], status_code=200)
def get_paginate_jobsarea_by_page_per_page(page:int, per_page: int):
    return models.JobsArea.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetJobsArea, status_code=200)
def get_jobsarea_by_uuid(uuid: UUID4):
    return models.JobsArea.get(uuid)

@router.post("/", response_model=schema.GetJobsArea, status_code=201)
def create_new_jobsarea(
    json_data: schema.PostJobsArea,
):
    data = models.JobsArea(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetJobsArea, status_code=200)
def update_jobsarea_by_uuid(uuid: UUID4, json_data: schema.PutJobsArea):
    return models.JobsArea.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_jobsarea_by_uuid(uuid: UUID4):
    return models.JobsArea.remove(uuid)

    