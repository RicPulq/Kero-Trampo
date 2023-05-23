from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/jobsprofile", tags=["JobsProfile"])


@router.get("/all/", response_model=List[schema.GetJobsProfile], status_code=200)
def get_all_jobsprofile():
    return models.JobsProfile.get_all()


@router.get("/paginate/", response_model=List[schema.GetJobsProfile], status_code=200)
def get_paginate_jobsprofile_by_page_per_page(page: int, per_page: int):
    return models.JobsProfile.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.GetJobsProfile, status_code=200)
def get_jobsprofile_by_uuid(uuid: UUID4):
    return models.JobsProfile.get(uuid)


@router.post("/", response_model=schema.GetJobsProfile, status_code=201)
def create_new_jobsprofile(json_data: List[schema.PostJobsProfile]):
    try:
        _db = db.Session()
        for data_json in json_data:
            data = models.JobsProfile(**data_json.dict())
            if not data:
                raise HTTPException(
                    status_code=404, detail=[{"msg": "dado não encontrado"}]
                )
            _db.add(data)
        _db.commit()
        _db.refresh(data)
    finally:
        _db.close()
    return "Ok"


@router.put("/uuid", response_model=schema.GetJobsProfile, status_code=200)
def update_jobsprofile_by_uuid(uuid: UUID4, json_data: schema.PutJobsProfile):
    return models.JobsProfile.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_jobsprofile_by_uuid(uuid: UUID4):
    return models.JobsProfile.remove(uuid)
