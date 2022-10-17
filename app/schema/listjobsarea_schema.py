from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from app.schema.jobsarea_schema import GetJobsArea
from app.schema.students_schema import GetStudents

__all__ = ['PostListJobsArea', 'GetListJobsArea', 'PutListJobsArea','ShowList']



class PostListJobsArea(BaseModel):
    student_uuid: UUID | None = Field(description='Student_uuid Documentar')
    jobs_area_uuid: UUID | None = Field(description='Jobs_area_uuid Documentar')
    others: str | None = Field(description="Onde o usuário vai declara uma opção que está fora da lista pré-populada")

    

class GetListJobsArea(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: UUID | None = Field(description='Student_uuid Documentar')
    jobs_area_uuid: UUID | None = Field(description='Jobs_area_uuid Documentar')
    others: str | None = Field(description="Onde o usuário vai declara uma opção que está fora da lista pré-populada")

    class Config:
        orm_mode = True


class ShowList(GetListJobsArea):
    jobsarea: GetJobsArea
    student: GetStudents

    class Config:
        orm_mode=True


class PutListJobsArea(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    jobs_area_uuid: str | None = Field(description='Jobs_area_uuid Documentar')
