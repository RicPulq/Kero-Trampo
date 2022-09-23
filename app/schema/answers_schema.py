from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostAnswers', 'GetAnswers', 'PutAnswers',]



class PostAnswers(BaseModel):
    answer: str | None = Field(description='Answer Documentar', max_length=255)
    bool_answer: bool | None = Field(description='Bool_answer Documentar')

    

class GetAnswers(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    answer: str | None = Field(description='Answer Documentar', max_length=255)
    bool_answer: bool | None = Field(description='Bool_answer Documentar')


    class Config:
        orm_mode = True



class PutAnswers(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    answer: str | None = Field(description='Answer Documentar', max_length=255)
    bool_answer: bool | None = Field(description='Bool_answer Documentar')
