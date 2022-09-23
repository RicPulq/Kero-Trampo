from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/jobsprofile", tags=["JobsProfile"])


@router.get("/all/", response_model=List[schema.GetJobsProfile], status_code=200)
def get_all_jobsprofile():
    return models.JobsProfile.get_all()

@router.get("/paginate/", response_model=List[schema.GetJobsProfile], status_code=200)
def get_paginate_jobsprofile_by_page_per_page(page:int, per_page: int):
    return models.JobsProfile.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetJobsProfile, status_code=200)
def get_jobsprofile_by_uuid(uuid: UUID4):
    return models.JobsProfile.get(uuid)

@router.post("/", response_model=schema.GetJobsProfile, status_code=201)
def create_new_jobsprofile(
    json_data: schema.PostJobsProfile,
):
    data = models.JobsProfile(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetJobsProfile, status_code=200)
def update_jobsprofile_by_uuid(uuid: UUID4, json_data: schema.PutJobsProfile):
    return models.JobsProfile.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_jobsprofile_by_uuid(uuid: UUID4):
    return models.JobsProfile.remove(uuid)

    