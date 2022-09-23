from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ['PostQuiz', 'GetQuiz', 'PutQuiz',]



class PostQuiz(BaseModel):
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    question_uuid: str | None = Field(description='Question_uuid Documentar')
    answer_uuid: str | None = Field(description='Answer_uuid Documentar')

    

class GetQuiz(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    question_uuid: str | None = Field(description='Question_uuid Documentar')
    answer_uuid: str | None = Field(description='Answer_uuid Documentar')


    class Config:
        orm_mode = True



class PutQuiz(BaseModel):
    uuid: UUID | None = Field(description='Uuid Documentar')
    creat_at: datetime | None = Field(description='Creat_at Documentar')
    updat_at: datetime | None = Field(description='Updat_at Documentar')
    student_uuid: str | None = Field(description='Student_uuid Documentar')
    question_uuid: str | None = Field(description='Question_uuid Documentar')
    answer_uuid: str | None = Field(description='Answer_uuid Documentar')
