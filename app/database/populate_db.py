from uuid import UUID
from app import models, schema

from .user import admin
from .role import role
from ..core.security import get_password_hash
from .answers import answers
from .employer_characteristics import employer_characteristics
from .field_activities import field_activities
from .hiring_problems import hiring_problems
from .job_profile import job_profile
from .jobs_area import jobs_area
from .pcd import pcds
from .previously_job import previously_job
from .questions import questions

def pop_db_init():
    for role_aux in role:
    # percorre toda a lista de dados "role"
        if not models.Role.query_com_dois_params("name",role_aux["name"],None,None):
        # verifica no banco se já existe os dados, caso não cria no banco as "roles" 
            role_schema = schema.PostRole
            role_schema = dict(role_aux)
            roles = models.Role(**role_schema)
            roles.create()
    if not models.User.query_com_dois_params("username",admin["username"],None,None):
    # verifica no banco se já existe o usuário "admin" e caso não cria
        admin["password"] = get_password_hash(admin["password"])
        admin["active"] = True
        aux_role = role[0]
        data_role = models.Role.query_com_dois_params("name",aux_role["name"],"permission_level",aux_role["permission_level"])
        admin["role_uuid"] = data_role.uuid
        user_schema = schema.PostUser(**admin)
        user = models.User(**user_schema.dict())
        user.create()
    
def pop_db():
    for answer in answers:
        if not models.Answers.query_com_dois_params("answer", answer["answer"],None,None):
            aux_answer = schema.PostAnswers(**answer)
            answer_data = models.Answers(**aux_answer.dict())  
            answer_data.create()       
    for characteristic in employer_characteristics:
        if not models.EmployerCharacteristics.query_com_dois_params("characteristc", characteristic, None,None):
            characteristic_data = models.EmployerCharacteristics(characteristc=characteristic)
            characteristic_data.create()
    for field in field_activities:
        if not models.FieldActivity.query_com_dois_params("activity", field, None,None):
            field_data = models.FieldActivity(activity=field)
            field_data.create()
    for problem in hiring_problems:
        if not models.HiringProblems.query_com_dois_params("problem", problem,None,None):
            problem_data = models.HiringProblems(problem=problem)
            problem_data.create()
    for profile in job_profile:
        if not models.JobsProfile.query_com_dois_params("name", profile,None,None):
            profile_data = models.JobsProfile(name=profile)
            profile_data.create()
    for area in jobs_area:
        if not models.JobsArea.query_com_dois_params("name", area, None, None):
            area_data = models.JobsArea(name=area)
            area_data.create()
    for pcd in pcds:
        if not models.Pcd.query_com_dois_params("name", pcd, None, None):
            pcd_data = models.Pcd(name=pcd)
            pcd_data.create()
    for previous in previously_job:
        if not models.PreviouslyJob.query_com_dois_params("name", previous, None, None):
            previous_data = models.PreviouslyJob(name=previous)
            previous_data.create()
    for question in questions:
        if not models.Questions.query_com_dois_params("questions", question, None, None):
            question_data = models.Questions(questions=question)
            question_data.create()