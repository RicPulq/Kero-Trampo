from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostListHiringProblems', 'GetListHiringProblems', 'PutListHiringProblems',]



class PostListHiringProblems(BaseModel):
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    problem_uuid: str | None = Field(description='Problem_uuid Documentar')

    

class GetListHiringProblems(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    problem_uuid: str | None = Field(description='Problem_uuid Documentar')


    class Config:
        orm_mode = True



class PutListHiringProblems(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    company_uuid: str | None = Field(description='Company_uuid Documentar')
    problem_uuid: str | None = Field(description='Problem_uuid Documentar')
