from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostQuestions', 'GetQuestions', 'PutQuestions',]



class PostQuestions(BaseModel):
    questions: str | None = Field(description='Questions Documentar', max_length=300)

    

class GetQuestions(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    questions: str | None = Field(description='Questions Documentar', max_length=255)


    class Config:
        orm_mode = True



class PutQuestions(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    questions: str | None = Field(description='Questions Documentar', max_length=255)
