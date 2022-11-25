from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from app.schema.company_schema import GetCompany
from app.schema.address_schema import GetAddress

__all__ = ["PostBranchOffice", "GetBranchOffice", "PutBranchOffice", "ShowBranch"]


class PostBranchOffice(BaseModel):
    # company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    # address_uuid: UUID | None = Field(description='Address_uuid Documentar')


class GetBranchOffice(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: UUID | None = Field(description="Company_uuid Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    address_uuid: UUID | None = Field(description="Address_uuid Documentar")

    class Config:
        orm_mode = True


class ShowBranch(GetBranchOffice):
    address: GetAddress
    company: GetCompany

    class Config:
        orm_mode = True


class PutBranchOffice(BaseModel):
    uuid: UUID | None = Field(description="Uuid Documentar")
    creat_at: datetime | None = Field(description="Creat_at Documentar")
    updat_at: datetime | None = Field(description="Updat_at Documentar")
    company_uuid: str | None = Field(description="Company_uuid Documentar")
    name: str | None = Field(description="Name Documentar", max_length=255)
    address_uuid: str | None = Field(description="Address_uuid Documentar")
