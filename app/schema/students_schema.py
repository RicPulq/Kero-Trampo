from typing import List
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from .academicprofiles_schema import (
    GetAcademicProfiles,
    PostAcademicProfiles,
    PutAcademicProfiles,
)
from .address_schema import GetAddress, PostAddress, PutAddress

__all__ = [
    "PostStudents",
    "GetStudents",
    "PutStudents",
    "ShowStudents",
    "UpdateStudent",
]


class PostStudents(BaseModel):
    name: str | None = Field(description="Nome do estudante", max_length=255)
    email: str | None = Field(description="Email do estudantes", max_length=255)
    birthdate: str | None = Field(description="Data de nascimento")
    marital_status: str | None = Field(description="Estado Civil", max_length=45)
    phone_number: str | None = Field(
        description="Número do telefone do estudante", max_length=255
    )
    availability: str | None = Field(
        description="Disponibilidade dos dados para empresas parceiras?", max_length=15
    )
    pcd: bool | None = Field(description="Estudante é PCD ou não")
    # user_uuid: UUID | None = Field(description='User_uuid Documentar')
    class Config:
        schema_extra = {
            "example": {
                "name": "Teste_extra_estudante",
                "email": "retik51803@fsouda.com",
                "birthdate": "13/11/2000",
                "marital_status": "solteiro",
                "phone_number": "65905492034",
                "availability": "sim",
                "pcd": False,
            }
        }


class GetStudents(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    email: str | None = Field(description="Email Documentar", max_length=255)
    birthdate: datetime | None = Field(description="Birthdate Documentar")
    marital_status: str | None = Field(
        description="Marital_status Documentar", max_length=45
    )
    phone_number: str | None = Field(
        description="Phone_number Documentar", max_length=255
    )
    availability: str | None = Field(
        description="Availability Documentar", max_length=15
    )
    pcd: bool | None = Field(description="Pcd Documentar")
    user_uuid: UUID | None = Field(description="User_uuid Documentar")

    class Config:
        orm_mode = True


class ShowStudents(GetStudents):
    address: GetAddress | None = Field(description="Endereço")
    academicprofiles: GetAcademicProfiles | None = Field(description="Perfil Acadêmico")

    class Config:
        orm_mode = True


class PutStudents(BaseModel):
    # uuid: UUID | None = Field(description="Uuid Documentar")
    # creat_at: datetime | None = Field(description="Creat_at Documentar")
    # updat_at: datetime | None = Field(description="Updat_at Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    email: str | None = Field(description="Email Documentar", max_length=255)
    birthdate: datetime | None = Field(description="Birthdate Documentar")
    marital_status: str | None = Field(
        description="Marital_status Documentar", max_length=45
    )
    phone_number: str | None = Field(
        description="Phone_number Documentar", max_length=255
    )
    availability: str | None = Field(
        description="Availability Documentar", max_length=15
    )
    pcd: bool | None = Field(description="Pcd Documentar")
    # user_uuid: UUID | None = Field(description='User_uuid Documentar')


class UpdateStudent(PutStudents):
    address: PutAddress
    academicprofiles: PutAcademicProfiles

    class Config:
        orm_mode = True
