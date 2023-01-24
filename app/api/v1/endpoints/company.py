from fastapi import APIRouter
from pydantic.types import UUID4
from typing import List

from ....core.security import get_password_hash
import app.templates as templates
import app.util as util
from app import schema, models, core

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("/all/", response_model=List[schema.GetCompany], status_code=200)
def get_all_company():
    return models.Company.get_all()


@router.get("/paginate/", response_model=List[schema.GetCompany], status_code=200)
def get_paginate_company_by_page_per_page(page: int, per_page: int):
    return models.Company.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowCompany, status_code=200)
def get_company_by_uuid(uuid: UUID4):
    return models.Company.get(uuid)


@router.post("/", response_model=schema.GetCompany, status_code=201)
def create_new_company(
    json_data: schema.PostCompany,
):
    data = models.Company(**json_data.dict())
    return data.create()


@router.post("/v2", response_model=schema.GetCompany, status_code=201)
def create_company_with_all(
    user: schema.PostUser,
    address: schema.PostAddress,
    company: schema.PostCompany,
    # address_branch: schema.PostAddress,
    # branch: List[schema.PostBranchOffice],
    hiring_problems: List[schema.PostListHiringProblems],
    characteristcs: List[schema.PostListCharacteristics],
    jobsprofile: List[schema.PostListJobProfile] | None,
    fieldactivity: List[schema.PostListFieldActivities],
    pcd: List[schema.PostCompanyPcd] | None,
):
    """Para criar uma filial, usar rota BranchOffice"""
    user.password = get_password_hash(user.password)
    data_company = models.Company(**company.dict())
    data_company.user = models.User(**user.dict())
    data_company.address = models.Address(**address.dict())
    # for data_branch in branch:
    #     data_company.branch.append(models.BranchOffice(**data_branch.dict()))
    #     data_company.branch.address=(models.Address(**address_branch.dict()))
    for data_hproblems in hiring_problems:
        data_company.list_hiring_problems.append(
            models.ListHiringProblems(**data_hproblems.dict())
        )
    for data_characteristics in characteristcs:
        data_company.list_characteristic.append(
            models.ListCharacteristics(**data_characteristics.dict())
        )
    if jobsprofile:
        for data_jobsprofile in jobsprofile:
            data_company.list_job_profile.append(
                models.ListJobProfile(**data_jobsprofile.dict())
            )
    for data_fieldactivity in fieldactivity:
        data_company.list_field_activities.append(
            models.ListFieldActivities(**data_fieldactivity.dict())
        )
    if pcd:
        for data_pcd in pcd:
            data_company.company_pcd.append(models.CompanyPcd(**data_pcd.dict()))

    return data_company.create(), util.send_email(
        company.email, core.settings.PROJECT_NAME, templates.conteudo
    )


@router.put("/uuid", response_model=schema.GetCompany, status_code=200)
def update_company_by_uuid(uuid: UUID4, json_data: schema.PutCompany):
    return models.Company.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_company_by_uuid(uuid: UUID4):
    return models.Company.remove(uuid)
