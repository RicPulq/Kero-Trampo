from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostHiringProblems', 'GetHiringProblems', 'PutHiringProblems',]



class PostHiringProblems(BaseModel):
    problem: str | None = Field(description='Problem Documentar', max_length=255)

    

class GetHiringProblems(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    problem: str | None = Field(description='Problem Documentar', max_length=255)


    class Config:
        orm_mode = True



class PutHiringProblems(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    problem: str | None = Field(description='Problem Documentar', max_length=255)
