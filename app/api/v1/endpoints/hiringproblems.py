from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from app import schema, models

router = APIRouter(prefix="/hiringproblems", tags=["HiringProblems"])


@router.get("/all/", response_model=List[schema.GetHiringProblems], status_code=200)
def get_all_hiringproblems():
    return models.HiringProblems.get_all()

@router.get("/paginate/", response_model=List[schema.GetHiringProblems], status_code=200)
def get_paginate_hiringproblems_by_page_per_page(page:int, per_page: int):
    return models.HiringProblems.get_paginate(page, per_page)

@router.get("/uuid", response_model=schema.GetHiringProblems, status_code=200)
def get_hiringproblems_by_uuid(uuid: UUID4):
    return models.HiringProblems.get(uuid)

@router.post("/", response_model=schema.GetHiringProblems, status_code=201)
def create_new_hiringproblems(
    json_data: schema.PostHiringProblems,
):
    data = models.HiringProblems(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetHiringProblems, status_code=200)
def update_hiringproblems_by_uuid(uuid: UUID4, json_data: schema.PutHiringProblems):
    return models.HiringProblems.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_hiringproblems_by_uuid(uuid: UUID4):
    return models.HiringProblems.remove(uuid)

    