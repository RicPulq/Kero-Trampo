from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostListPreviouslyJobs', 'GetListPreviouslyJobs', 'PutListPreviouslyJobs',]



class PostListPreviouslyJobs(BaseModel):
    # student_uuid: UUID | None = Field(description='Student_uuid Documentar')
    prev_job_uuid: UUID | None = Field(description='Prev_job_uuid Documentar')
    others: str | None = Field(description='Onde o usuário vai declara uma opção que está fora da lista pré-populada')

    

class GetListPreviouslyJobs(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: UUID | None = Field(description='Student_uuid Documentar')
    prev_job_uuid: UUID | None = Field(description='Prev_job_uuid Documentar')


    class Config:
        orm_mode = True



class PutListPreviouslyJobs(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: UUID | None = Field(description='Student_uuid Documentar')
    prev_job_uuid: UUID | None = Field(description='Prev_job_uuid Documentar')
