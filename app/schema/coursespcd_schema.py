from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostCoursesPCD', 'GetCoursesPCD', 'PutCoursesPCD',]



class PostCoursesPCD(BaseModel):
    courses_uuid: UUID | None = Field(description='Courses_uuid Documentar')
    pcd_uuid: UUID | None = Field(description='Pcd_uuid Documentar')



class GetCoursesPCD(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    courses_uuid: UUID | None = Field(description='Courses_uuid Documentar')
    pcd_uuid: UUID | None = Field(description='Pcd_uuid Documentar')


    class Config:
        orm_mode = True



class PutCoursesPCD(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    courses_uuid: UUID | None = Field(description='Courses_uuid Documentar')
    pcd_uuid: UUID | None = Field(description='Pcd_uuid Documentar')
