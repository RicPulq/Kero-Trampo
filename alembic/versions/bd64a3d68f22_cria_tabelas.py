"""cria_tabelas

Revision ID: bd64a3d68f22
Revises: e70740b43367
Create Date: 2023-06-22 16:54:44.364312

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bd64a3d68f22'
down_revision = 'e70740b43367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('academicprofiles',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('education_instution', sa.String(length=255), nullable=False),
    sa.Column('campus_name', sa.String(length=255), nullable=False),
    sa.Column('city_instution', sa.String(length=255), nullable=False),
    sa.Column('course_name', sa.String(length=255), nullable=False),
    sa.Column('type_institution', sa.String(length=45), nullable=False),
    sa.Column('teaching_modality', sa.String(length=45), nullable=False),
    sa.Column('other_courses', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('address',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('street', sa.String(length=255), nullable=True),
    sa.Column('number', sa.String(length=15), nullable=True),
    sa.Column('complement', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('country', sa.String(length=35), nullable=True),
    sa.Column('district', sa.String(length=50), nullable=True),
    sa.Column('cep', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('answers',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('answer', sa.String(length=255), nullable=False),
    sa.Column('bool_answer', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('employercharacteristics',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('characteristc', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('fieldactivity',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('activity', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('hiringproblems',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('problem', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('jobsarea',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('jobsprofile',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('pcd',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('previouslyjob',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('questions',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('questions', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('role',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permission_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('campus',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name_institution', sa.String(length=255), nullable=False),
    sa.Column('type_institution', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['address_uuid'], ['address.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('user',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('role_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['role_uuid'], ['role.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('username')
    )
    op.create_table('company',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('number_employers', sa.Integer(), nullable=True),
    sa.Column('opening_hours', sa.String(length=255), nullable=False),
    sa.Column('work_style', sa.Integer(), nullable=True),
    sa.Column('hiring', sa.Boolean(), nullable=True),
    sa.Column('pcd', sa.Boolean(), nullable=True),
    sa.Column('link_site', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=255), nullable=False),
    sa.Column('user_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('address_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['address_uuid'], ['address.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('courses',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('modality', sa.String(length=255), nullable=False),
    sa.Column('annual_graduates', sa.Integer(), nullable=True),
    sa.Column('pcd', sa.Boolean(), nullable=True),
    sa.Column('employability_index', sa.Float(), nullable=True),
    sa.Column('businessperson_index', sa.Float(), nullable=True),
    sa.Column('public_server_index', sa.Float(), nullable=True),
    sa.Column('link_site', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=255), nullable=False),
    sa.Column('user_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('campus_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['campus_uuid'], ['campus.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('students',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('number_children', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('birthdate', sa.String(length=255), nullable=False),
    sa.Column('marital_status', sa.String(length=45), nullable=False),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('availability', sa.String(length=15), nullable=False),
    sa.Column('curriculum', sa.String(length=255), nullable=False),
    sa.Column('pcd', sa.Boolean(), nullable=True),
    sa.Column('user_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('address_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('academic_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['academic_uuid'], ['academicprofiles.uuid'], ),
    sa.ForeignKeyConstraint(['address_uuid'], ['address.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('branchoffice',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('company_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('address_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['address_uuid'], ['address.uuid'], ),
    sa.ForeignKeyConstraint(['company_uuid'], ['company.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('companypcd',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('company_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pcd_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['company_uuid'], ['company.uuid'], ),
    sa.ForeignKeyConstraint(['pcd_uuid'], ['pcd.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('coursespcd',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('courses_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pcd_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['courses_uuid'], ['courses.uuid'], ),
    sa.ForeignKeyConstraint(['pcd_uuid'], ['pcd.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('listcharacteristics',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('company_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('characteristic_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['characteristic_uuid'], ['employercharacteristics.uuid'], ),
    sa.ForeignKeyConstraint(['company_uuid'], ['company.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('listfieldactivities',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('company_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('field_activity_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['company_uuid'], ['company.uuid'], ),
    sa.ForeignKeyConstraint(['field_activity_uuid'], ['fieldactivity.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('listhiringproblems',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('company_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('hiring_problems_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['company_uuid'], ['company.uuid'], ),
    sa.ForeignKeyConstraint(['hiring_problems_uuid'], ['hiringproblems.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('listjobprofile',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('company_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('job_profile_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['company_uuid'], ['company.uuid'], ),
    sa.ForeignKeyConstraint(['job_profile_uuid'], ['jobsprofile.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('listjobsarea',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('student_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('jobs_area_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['jobs_area_uuid'], ['jobsarea.uuid'], ),
    sa.ForeignKeyConstraint(['student_uuid'], ['students.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('listpreviouslyjobs',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('student_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('prev_job_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['prev_job_uuid'], ['previouslyjob.uuid'], ),
    sa.ForeignKeyConstraint(['student_uuid'], ['students.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('quiz',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('students_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('questions_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('answers_uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['answers_uuid'], ['answers.uuid'], ),
    sa.ForeignKeyConstraint(['questions_uuid'], ['questions.uuid'], ),
    sa.ForeignKeyConstraint(['students_uuid'], ['students.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('studentspcd',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creat_at', sa.DateTime(), nullable=False),
    sa.Column('updat_at', sa.DateTime(), nullable=True),
    sa.Column('students_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pcd_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('others', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['pcd_uuid'], ['pcd.uuid'], ),
    sa.ForeignKeyConstraint(['students_uuid'], ['students.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('studentspcd')
    op.drop_table('quiz')
    op.drop_table('listpreviouslyjobs')
    op.drop_table('listjobsarea')
    op.drop_table('listjobprofile')
    op.drop_table('listhiringproblems')
    op.drop_table('listfieldactivities')
    op.drop_table('listcharacteristics')
    op.drop_table('coursespcd')
    op.drop_table('companypcd')
    op.drop_table('branchoffice')
    op.drop_table('students')
    op.drop_table('courses')
    op.drop_table('company')
    op.drop_table('user')
    op.drop_table('campus')
    op.drop_table('role')
    op.drop_table('questions')
    op.drop_table('previouslyjob')
    op.drop_table('pcd')
    op.drop_table('jobsprofile')
    op.drop_table('jobsarea')
    op.drop_table('hiringproblems')
    op.drop_table('fieldactivity')
    op.drop_table('employercharacteristics')
    op.drop_table('answers')
    op.drop_table('address')
    op.drop_table('academicprofiles')
    # ### end Alembic commands ###

