from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostListJobsArea', 'GetListJobsArea', 'PutListJobsArea',]



class PostListJobsArea(BaseModel):
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    jobs_area_uuid: str | None = Field(description='Jobs_area_uuid Documentar')

    

class GetListJobsArea(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    jobs_area_uuid: str | None = Field(description='Jobs_area_uuid Documentar')


    class Config:
        orm_mode = True



class PutListJobsArea(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    jobs_area_uuid: str | None = Field(description='Jobs_area_uuid Documentar')
