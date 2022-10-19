from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/listhiringproblems", tags=["ListHiringProblems"])


@router.get("/all/", response_model=List[schema.GetListHiringProblems], status_code=200)
def get_all_listhiringproblems():
    return models.ListHiringProblems.get_all()


@router.get(
    "/paginate/", response_model=List[schema.GetListHiringProblems], status_code=200
)
def get_paginate_listhiringproblems_by_page_per_page(page: int, per_page: int):
    return models.ListHiringProblems.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowListProblems, status_code=200)
def get_listhiringproblems_by_uuid(uuid: UUID4):
    return models.ListHiringProblems.get(uuid)


@router.post("/", response_model=schema.GetListHiringProblems, status_code=201)
def create_new_listhiringproblems(
    json_data: List[schema.PostListHiringProblems],
):
    try:
        _db = db.Session()
        for data_list in json_data:
            data = models.ListHiringProblems(**data_list.dict())
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


@router.put("/uuid", response_model=schema.GetListHiringProblems, status_code=200)
def update_listhiringproblems_by_uuid(
    uuid: UUID4, json_data: schema.PutListHiringProblems
):
    return models.ListHiringProblems.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_listhiringproblems_by_uuid(uuid: UUID4):
    return models.ListHiringProblems.remove(uuid)
