from tkinter import W
from fastapi import APIRouter, HTTPException
from pydantic.types import UUID4
from typing import List
from app import db

from app import schema, models

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/all/", response_model=List[schema.GetStudents], status_code=200)
def get_all_students():
    return models.Students.get_all()


@router.get("/paginate/", response_model=List[schema.GetStudents], status_code=200)
def get_paginate_students_by_page_per_page(page: int, per_page: int):
    return models.Students.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowStudents, status_code=200)
def get_students_by_uuid(uuid: UUID4):
    return models.Students.get(uuid)


@router.post("/", response_model=schema.GetStudents, status_code=201)
def create_new_students(
    json_data: schema.PostStudents,
):
    data = models.Students(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetStudents, status_code=200)
def update_students_by_uuid(uuid: UUID4, json_data: schema.PutStudents):
    return models.Students.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_students_by_uuid(uuid: UUID4):
    return models.Students.remove(uuid)


# @router.post("/User_and_Student", status_code=200)
# def post_user_with_students(user: schema.PostUser, students: schema.PostStudents):
#     user_data = models.User(**user.dict())
#     user_data.students_relation.append(models.Students(**students.dict()))
#     return user_data.create()


@router.delete("/delete_User_Student", status_code=200)
def delete_user_student_address(uuid: UUID4):
    """Utilizar o UUID do Student"""
    return models.User.remove(uuid)


@router.post("/user_student_address_academicprofile", status_code=200)
def create_user_student_address_academicprofile(
    user: schema.PostUser,
    address: schema.PostAddress,
    student: schema.PostStudents,
    academic: schema.PostAcademicProfiles,
    # quiz: schema.PostQuiz
):
    """Rota para criar toda a ficha do egressista"""
    # data_student.ad.append(models.Address(**address.dict()))
    data_academic = models.AcademicProfiles(**academic.dict())
    data_student = models.Students(**student.dict())
    data_address = models.Address(**address.dict())
    data_user = models.User(**user.dict())
    # data_quiz = models.Quiz(**quiz.dict())

    data_academic.students.append(data_student)
    data_address.relation_students.append(data_student)
    data_user.students_relation.append(data_student)

    print(data_academic,data_address,data_student)

    # data_quiz.student.append()
    # data_quiz.questions.append()
    # data_quiz.answers.append()


    return data_address.create(), data_user.create(), data_academic.create()


@router.put("/user_student_address_academicprofile", status_code=200)
def update_user_student_address_academicprofile(
    uuid: UUID4,
    # data: schema.UpdateUser,
    user: schema.PutUser,
    student: schema.PutStudents,
):

    try:
        _db = db.Session()
        data_user = _db.query(models.User).filter_by(uuid=uuid).first()
        if not data_user:
            raise HTTPException(
                status_code=404, detail=[{"msg": "Dado não encontrado"}]
            )
        print(data_user)
        for key, value in user.dict(exclude_unset=True).items():
            setattr(data_user, key, value)
        print("=" * 10)

        data_student = _db.query(models.Students).filter_by(user_uuid=uuid).first()

        if not data_student:
            raise HTTPException(
                status_code=404, detail=[{"msg": "Dado não encontrado"}]
            )
        for key, value in student.dict(exclude_unset=True).items():
            setattr(data_student, key, value)

        _db.add(data_user)
        _db.add(data_student)
        _db.commit()
        _db.refresh(data_user)
    except:
        _db.rollback()
    finally:
        _db.close()

    return data_user
