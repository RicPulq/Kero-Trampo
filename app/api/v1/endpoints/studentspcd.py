from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List

from app import schema, models, db

router = APIRouter(prefix="/studentspcd", tags=["StudentsPcd"])


@router.get("/all/", response_model=List[schema.GetStudentsPcd], status_code=200)
def get_all_studentspcd():
    return models.StudentsPcd.get_all()


@router.get("/paginate/", response_model=List[schema.GetStudentsPcd], status_code=200)
def get_paginate_studentspcd_by_page_per_page(page: int, per_page: int):
    return models.StudentsPcd.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowPCDs, status_code=200)
def get_studentspcd_by_uuid(uuid: UUID4):
    return models.StudentsPcd.get(uuid)


@router.get("/students_uuid", response_model=List[schema.ShowPCDs], status_code=200)
def get_pcds_by_students_uuid(uuid: UUID4):
    try:
        _db = db.Session()
        data = _db.query(models.StudentsPcd).filter_by(students_uuid=uuid).all()
        if not data:
            raise HTTPException(
                status_code=404, detail=[{"msg": "dado não encontrado"}]
            )
    finally:
        _db.close()
    return data


@router.post("/", response_model=schema.GetStudentsPcd, status_code=201)
def create_new_studentspcd(
    json_data: List[schema.PostStudentsPcd],
):

    _db = db.Session()
    for data_list in json_data:
        data = models.StudentsPcd(**data_list.dict())
        _db.add(data)
    _db.commit()
    _db.refresh(data)
    _db.close()
    return data


@router.put("/uuid", response_model=schema.GetStudentsPcd, status_code=200)
def update_studentspcd_by_uuid(uuid: UUID4, json_data: schema.PutStudentsPcd):
    return models.StudentsPcd.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_studentspcd_by_uuid(uuid: UUID4):
    return models.StudentsPcd.remove(uuid)
