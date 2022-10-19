from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from app.schema.company_schema import GetCompany

from app.schema.jobsprofile_schema import GetJobsProfile

__all__ = [
    "PostListJobProfile",
    "GetListJobProfile",
    "PutListJobProfile",
    "ShowJobs"
]


class PostListJobProfile(BaseModel):
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    job_profile_uuid: UUID | None = Field(description="Job_profile_uuid Documentar")
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )


class GetListJobProfile(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    job_profile_uuid: UUID | None = Field(description="Job_profile_uuid Documentar")
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )

    class Config:
        orm_mode = True


class ShowJobs(GetListJobProfile):
    job_profile: GetJobsProfile
    company: GetCompany
    class Config:
        orm_mode=True



class PutListJobProfile(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    # company_uuid: UUID | None = Field(description='Company_uuid Documentar')
    job_profile_uuid: UUID | None = Field(description="Job_profile_uuid Documentar")
