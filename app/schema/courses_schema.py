from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from app.schema.campus_schema import GetCampus, ShowCampus

__all__ = [
    "PostCourses",
    "GetCourses",
    "PutCourses",
]


class PostCourses(BaseModel):
    # campus_uuid: UUID | None = Field(description='UUID do campus ao qual o curso pertence')
    name: str | None = Field(description="Name Documentar", max_length=255)
    modality: str | None = Field(description="Modality Documentar", max_length=255)
    annual_graduates: int | None = Field(description="Annual_graduates Documentar")
    pcd: bool | None = Field(description="Pcd Documentar")
    employability_index: int | None = Field(
        description="Employability_index Documentar"
    )
    businessperson_index: int | None = Field(
        description="Businessperson_index Documentar"
    )
    public_server_index: int | None = Field(
        description="Public_server_index Documentar"
    )
    link_site: str | None = Field(description="Link_site Documentar", max_length=255)
    email: str | None = Field(description="Email Documentar", max_length=255)
    phone_number: str | None = Field(
        description="Phone_number Documentar", max_length=255
    )


class GetCourses(BaseModel):
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    user_uuid: str | None = Field(description="User_uuid Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    modality: str | None = Field(description="Modality Documentar", max_length=255)
    annual_graduates: int | None = Field(description="Annual_graduates Documentar")
    pcd: bool | None = Field(description="Pcd Documentar")
    employability_index: int | None = Field(
        description="Employability_index Documentar"
    )
    businessperson_index: int | None = Field(
        description="Businessperson_index Documentar"
    )
    public_server_index: int | None = Field(
        description="Public_server_index Documentar"
    )
    link_site: str | None = Field(description="Link_site Documentar", max_length=255)
    email: str | None = Field(description="Email Documentar", max_length=255)
    phone_number: str | None = Field(
        description="Phone_number Documentar", max_length=255
    )
    user_uuid: UUID | None = Field(description="User_uuid Documentar")

    class Config:
        orm_mode = True


class PutCourses(BaseModel):

    # user_uuid: UUID | None = Field(description="User_uuid Documentar")
    # creat_at: datetime | None = Field(description="Creat_at Documentar")
    # updat_at: datetime | None = Field(description="Updat_at Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    modality: str | None = Field(description="Modality Documentar", max_length=255)
    annual_graduates: int | None = Field(description="Annual_graduates Documentar")
    pcd: bool | None = Field(description="Pcd Documentar")
    employability_index: int | None = Field(
        description="Employability_index Documentar"
    )
    businessperson_index: int | None = Field(
        description="Businessperson_index Documentar"
    )
    public_server_index: int | None = Field(
        description="Public_server_index Documentar"
    )
    link_site: str | None = Field(description="Link_site Documentar", max_length=255)
    email: str | None = Field(description="Email Documentar", max_length=255)
    phone_number: str | None = Field(
        description="Phone_number Documentar", max_length=255
    )


class ShowCourses(GetCourses):
    campus: ShowCampus | None = Field(description="Campus o qual o curso pertence")

    class Config:
        orm_mode = True
