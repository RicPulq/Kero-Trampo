from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List
from app import db
from app.auth import auth

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
def update_students_by_uuid(
    uuid: UUID4, json_data: schema.PutStudents, current_user: str = Depends(auth.Key.n1)
):
    print(current_user)
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
def delete_user_student_and_all(uuid: UUID4, current_user: str = Depends(auth.Key.n5)):
    print(current_user)
    """Utilizar o UUID do Student"""
    return models.User.remove(uuid)


@router.post("/student_with_all", status_code=200)
def create_student_with_all(
    user: schema.PostUser,
    address: schema.PostAddress,
    student: schema.PostStudents,
    academic_profile: schema.PostAcademicProfiles,
    quiz: List[schema.PostQuiz],
    jobs_area: List[schema.PostListJobsArea],
    prev_jobs: List[schema.PostListPreviouslyJobs]
):
    """Rota para criar toda a ficha do egressista"""
    # data_student.ad.append(models.Address(**address.dict()))
    data_student = models.Students(**student.dict())
    
    data_student.address = models.Address(**address.dict())
    data_student.academicprofiles = models.AcademicProfiles(**academic_profile.dict())
    data_student.user = models.User(**user.dict())
    for data_quiz in quiz:
        data_student.quiz.append(models.Quiz(**data_quiz.dict()))
    for data_jobsarea in jobs_area:
        data_student.list_jobsarea.append(models.ListJobsArea(**data_jobsarea.dict()))
    for data_prevjobs in prev_jobs:
        data_student.list_previouslyjobs.append(models.ListPreviouslyJobs(**data_prevjobs.dict()))


    return data_student.create()
