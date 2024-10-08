from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from app.schema.answers_schema import GetAnswers
from app.schema.questions_schema import GetQuestions

from app.schema.students_schema import GetStudents

__all__ = ["PostQuiz", "GetQuiz", "PutQuiz", "ShowQuiz"]


class PostQuiz(BaseModel):
    # students_uuid: UUID | None = Field(description="Student_uuid Documentar")
    questions_uuid: UUID | None = Field(description="Question_uuid Documentar")
    answers_uuid: UUID | None = Field(description="Answer_uuid Documentar")
    others: str | None = Field(description="Outros")
    class Config:
        schema_extra = {
            "example": {
                "questions_uuid": "bd6ecd24-99b5-4283-b173-baabc74b2f68",
                "answers_uuid": "34b701d3-cfbb-4924-89ac-c6e1a6f3fa2e",
                "others": ""
            }
        }


class GetQuiz(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    students_uuid: UUID | None = Field(description="Student_uuid Documentar")
    questions_uuid: UUID | None = Field(description="Question_uuid Documentar")
    answers_uuid: UUID | None = Field(description="Answer_uuid Documentar")
    others: str | None = Field(description="Outros")

    class Config:
        orm_mode = True


class ShowQuiz(GetQuiz):
    questions: GetQuestions
    answers: GetAnswers
    student: GetStudents

    class Config:
        orm_mode = True


class PutQuiz(BaseModel):
    # uuid: UUID | None = Field(description='Uuid Documentar')
    # creat_at: datetime | None = Field(description='Creat_at Documentar')
    # updat_at: datetime | None = Field(description='Updat_at Documentar')
    # students_uuid: UUID | None = Field(description='Student_uuid Documentar')
    # questions_uuid: UUID | None = Field(description='Question_uuid Documentar')
    answers_uuid: UUID | None = Field(description="Answer_uuid Documentar")
    others: str | None = Field(description="Outros")
