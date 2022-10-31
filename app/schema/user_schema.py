from uuid import UUID
from pydantic import BaseModel, Field, validator
from app import util
from datetime import datetime
from .students_schema import UpdateStudent, ShowStudents
from .company_schema import ShowCompany
from .courses_schema import ShowCourses
from typing import List

__all__ = ["PostUser", "GetUser", "PutUser", "ShowUser", "UpdateUser"]


class PostUser(BaseModel):
    username: str | None = Field(
        description="Username: email do usuário ", max_length=255
    )
    password: str | None = Field(
        description="Password: hash de 255 caracteres", max_length=255
    )
    active: bool | None = Field(
        description="Active: conta ativa ou não, para previnir spam de contas com o mesmo email"
    )
    role_uuid: UUID | None = Field(
        description="Uuid do nível de permissão de acesso do usuário"
    )
    _normalize_nome = validator("username", allow_reuse=True)(util.normalize_lower)


class GetUser(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    username: str | None = Field(description="Username Documentar", max_length=255)
    # password: str | None = Field(description="Password Documentar", max_length=255)
    active: bool | None = Field(description="Active Documentar")
    role_uuid: UUID | None = Field(description="Role_uuid Documentar")

    class Config:
        orm_mode = True


class ShowUser(GetUser):
    company_relation: List[ShowCompany] | None
    students_relation: List[ShowStudents] | None = Field(
        description="Objeto Estudante, que contem outros dois objetos: Endereço e Perfil Acadêmico"
    )
    courses_relation: List[ShowCourses] | None = Field(
        description="Objeto Cursos que contem o objeto Campus (que dentro contem o objeto: Endereço)"
    )

    class Config:
        orm_mode = True


class PutUser(BaseModel):

    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    username: str | None = Field(description="Username Documentar", max_length=255)
    password: str | None = Field(description="Password Documentar", max_length=255)
    active: bool | None = Field(description="estado do usuário, ativo ou desativado")
    role_uuid: UUID | None = Field(description="Role_uuid Documentar")

    _normalize_nome = validator("username", allow_reuse=True)(util.normalize_lower)


class UpdateUser(PutUser):
    students_relation: UpdateStudent

    class Config:
        orm_mode = True
