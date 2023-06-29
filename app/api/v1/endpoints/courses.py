from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List

from ....core.security import get_password_hash
import app.templates as templates
from app.auth import auth
import app.util as util
from app import schema, models, core

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/all/", response_model=List[schema.GetCourses], status_code=200)
def get_all_courses():
    return models.Courses.get_all()


@router.get("/paginate/", response_model=List[schema.GetCourses], status_code=200)
def get_paginate_courses_by_page_per_page(page: int, per_page: int):
    return models.Courses.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowCourses, status_code=200)
def get_courses_by_uuid(uuid: UUID4):
    return models.Courses.get(uuid)


@router.post("/", response_model=schema.GetCourses, status_code=201)
def create_new_courses(
    user: schema.PostUser,
    address: schema.PostAddress,
    campus: schema.PostCampus,
    course: schema.PostCourses,
    pcd: List[schema.PostCoursesPCD] | None,
):
    try:
        user.password = get_password_hash(user.password)
        data_course = models.Courses(**course.dict())

        data_course.user = models.User(**user.dict())
        data_course.campus = models.Campus(**campus.dict())
        data_course.campus.address = models.Address(**address.dict())
        for data_pcd in pcd:
            data_course.coursespcd.append(models.CoursesPCD(**data_pcd.dict()))

        return data_course.create(), util.send_email(
            course.email, core.settings.PROJECT_NAME, templates.conteudo
        )
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=f"Erro ao cadastrar, {e}")



@router.put("/uuid", response_model=schema.GetCourses, status_code=200)
def update_courses_by_uuid(uuid: UUID4, json_data: schema.PutCourses):
    return models.Courses.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_courses_by_uuid(uuid: UUID4, current_user: str = Depends(auth.Key.n2)):
    try:
        if current_user["user_uuid"] == str(uuid) or 5 in current_user["key"]:
            return models.User.remove(uuid)
        else:
            raise HTTPException(
            status_code=401,
            detail=[
                {"msg": "Desculpe Você nao tem Permissão, Chave de acesso expirada!"}
            ],
        )
    except:
        raise HTTPException(
            status_code=401,
            detail=[
                {"msg": "Desculpe Você nao tem Permissão, Chave de acesso expirada!"}
            ],
        )
    