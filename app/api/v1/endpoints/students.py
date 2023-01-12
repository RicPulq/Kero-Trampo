from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List
from app import db
from app.auth import auth
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app import schema, models, core

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/all/", response_model=List[schema.GetStudents], status_code=200)
def get_all_students():
    return models.Students.get_all()


@router.get("/paginate/", response_model=List[schema.GetStudents], status_code=200)
def get_paginate_students_by_page_per_page(page: int, per_page: int):
    return models.Students.get_paginate(page, per_page)


@router.get("/uuid", response_model=schema.ShowStudents, status_code=200)
def get_students_by_uuid(uuid: UUID4):
    return models.Students.get(uuid)


@router.post("/", response_model=schema.GetStudents, status_code=201)
def create_new_students(
    json_data: schema.PostStudents,
):
    data = models.Students(**json_data.dict())
    return data.create()


@router.put("/uuid", response_model=schema.GetStudents, status_code=200)
def update_students_by_uuid(
    uuid: UUID4, json_data: schema.PutStudents, current_user: str = Depends(auth.Key.n1)
):
    print(current_user)
    return models.Students.update(uuid, **json_data.dict(exclude_unset=True))


@router.delete("/uuid", status_code=204)
def delete_students_by_uuid(uuid: UUID4):
    return models.Students.remove(uuid)


# @router.post("/User_and_Student", status_code=200)
# def post_user_with_students(user: schema.PostUser, students: schema.PostStudents):
#     user_data = models.User(**user.dict())
#     user_data.students_relation.append(models.Students(**students.dict()))
#     return user_data.create()


@router.delete("/delete_User_Student", status_code=200)
def delete_user_student_and_all(uuid: UUID4, current_user: str = Depends(auth.Key.n5)):
    print(current_user)
    """Utilizar o UUID do Student"""
    return models.User.remove(uuid)


@router.post("/student_with_all", status_code=200)
def create_student_with_all(
    user: schema.PostUser,
    address: schema.PostAddress,
    student: schema.PostStudents,
    academic_profile: schema.PostAcademicProfiles,
    quiz: List[schema.PostQuiz],
    jobs_area: List[schema.PostListJobsArea],
    prev_jobs: List[schema.PostListPreviouslyJobs]
):
    """Rota para criar toda a ficha do egressista"""
    # data_student.ad.append(models.Address(**address.dict()))
    data_student = models.Students(**student.dict())
    
    data_student.address = models.Address(**address.dict())
    data_student.academicprofiles = models.AcademicProfiles(**academic_profile.dict())
    data_student.user = models.User(**user.dict())
    for data_quiz in quiz:
        data_student.quiz.append(models.Quiz(**data_quiz.dict()))
    for data_jobsarea in jobs_area:
        data_student.list_jobsarea.append(models.ListJobsArea(**data_jobsarea.dict()))
    for data_prevjobs in prev_jobs:
        data_student.list_previouslyjobs.append(models.ListPreviouslyJobs(**data_prevjobs.dict()))

    conteudo = """
    <html>
    <head>
    <style type="text/css">
        a {color: #d80a3e;}
    body, #header h1, #header h2, p {margin: 0; padding: 0;}
    #main {border: 1px solid #cfcece;}
    img {display: block;}
    #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
    #header h2 {color: #000000 !important; font-family: "Lucida Grande", sans-serif; font-size: 2px; }
    #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
    #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
    h5 {margin: 0 0 0.8em 0;}
        h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
    p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
    </style>
    </head>
    <body>
        <h2> UniEmpregos </h2>
    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td> 
        <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
            <tr>
                <td>
                    <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
                    <tr>
                        <td width="570" align="center"  bgcolor="#d80a3e"><h1>Inscrição Realizada Com Sucesso</h1></td>
                    </tr>
                    <tr>
                        <td width="570" align="right" bgcolor="#d80a3e"><p>November 2017</p></td>
                    </tr>
                    </table>
                </td>
            </tr>
        </table>
    </td></tr></table><!-- wrapper -->
    
    </body>
    </html>
    """
    password = core.config.settings.SMTP_PASSWORD
    msg = MIMEMultipart()
    msg['Subject'] = "UniEmpregos"
    msg['From'] = core.config.settings.SMTP_USER
    msg['To'] = student.email
    msg.attach(MIMEText(conteudo, 'html'))

    with smtplib.SMTP_SSL(host='smtp.gmail.com', timeout=5, port=465) as smtp:
        smtp.starttls
        smtp.login(msg['From'], password)
        smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        smtp.quit()
        print('enviado')

    return data_student.create()
