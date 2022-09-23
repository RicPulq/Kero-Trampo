from fastapi import APIRouter

from .listfieldactivities import router as listfieldactivities_router
from .companypcd import router as companypcd_router
from .address import router as address_router
from .listcharacteristics import router as listcharacteristics_router
from .developer import router as developer_router
from .students import router as students_router
from .user import router as user_router
from .jobsprofile import router as jobsprofile_router
from .answers import router as answers_router
from .coursespcd import router as coursespcd_router
from .campus import router as campus_router
from .jobsarea import router as jobsarea_router
from .role import router as role_router
from .login import router as login_router
from .listpreviouslyjobs import router as listpreviouslyjobs_router
from .company import router as company_router
from .quiz import router as quiz_router
from .studentspcd import router as studentspcd_router
from .pcd import router as pcd_router
from .listjobprofile import router as listjobprofile_router
from .hiringproblems import router as hiringproblems_router
from .courses import router as courses_router
from .listjobsarea import router as listjobsarea_router
from .questions import router as questions_router
from .fieldactivity import router as fieldactivity_router
from .branchoffice import router as branchoffice_router
from .listhiringproblems import router as listhiringproblems_router
from .employercharacteristics import router as employercharacteristics_router
from .previouslyjob import router as previouslyjob_router
from .academicprofiles import router as academicprofiles_router


routers = APIRouter()

routers.include_router(listfieldactivities_router)
routers.include_router(companypcd_router)
routers.include_router(address_router)
routers.include_router(listcharacteristics_router)
routers.include_router(developer_router)
routers.include_router(students_router)
routers.include_router(user_router)
routers.include_router(jobsprofile_router)
routers.include_router(answers_router)
routers.include_router(coursespcd_router)
routers.include_router(campus_router)
routers.include_router(jobsarea_router)
routers.include_router(role_router)
routers.include_router(login_router)
routers.include_router(listpreviouslyjobs_router)
routers.include_router(company_router)
routers.include_router(quiz_router)
routers.include_router(studentspcd_router)
routers.include_router(pcd_router)
routers.include_router(listjobprofile_router)
routers.include_router(hiringproblems_router)
routers.include_router(courses_router)
routers.include_router(listjobsarea_router)
routers.include_router(questions_router)
routers.include_router(fieldactivity_router)
routers.include_router(branchoffice_router)
routers.include_router(listhiringproblems_router)
routers.include_router(employercharacteristics_router)
routers.include_router(previouslyjob_router)
routers.include_router(academicprofiles_router)
