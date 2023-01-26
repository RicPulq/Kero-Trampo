from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from app.schema.company_schema import GetCompany

from app.schema.hiringproblems_schema import GetHiringProblems

__all__ = [
    "PostListHiringProblems",
    "GetListHiringProblems",
    "PutListHiringProblems",
    "ShowListProblems",
]


class PostListHiringProblems(BaseModel):
    # company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    hiring_problems_uuid: UUID | None = Field(description="Problem_uuid Documentar")
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )
    class Config:
            schema_extra = {
                "example": {
                    "hiring_problems_uuid": "a78af218-83cb-478b-8e9a-4f3a4946cdd3",
                    "others": ""
                }
            }


class GetListHiringProblems(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    hiring_problems_uuid: UUID | None = Field(description="Problem_uuid Documentar")
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )

    class Config:
        orm_mode = True


class ShowListProblems(GetListHiringProblems):
    hiring_problems: GetHiringProblems | None = Field(description="Instância um objeto Hiring Problems com os dados do UUID do problema fornecido")
    company: GetCompany | None = Field(description="Instância um objeto Company com os dados do UUID da compania fornecido")

    class Config:
        orm_mode = True


class PutListHiringProblems(BaseModel):
    # uuid: UUID | None = Field(description="Uuid Documentar")
    # creat_at: datetime | None = Field(description="Creat_at Documentar")
    # updat_at: datetime | None = Field(description="Updat_at Documentar")
    # company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    hiring_problems_uuid: UUID | None = Field(description="Problem_uuid Documentar")
    others: str | None = Field(
        description="Onde o usuário vai declara uma opção que está fora da lista pré-populada"
    )
