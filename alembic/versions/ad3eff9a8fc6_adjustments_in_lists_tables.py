"""adjustments_in_Lists_tables

Revision ID: ad3eff9a8fc6
Revises: 3ce2db584f9a
Create Date: 2022-10-17 16:58:11.910187

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ad3eff9a8fc6'
down_revision = '3ce2db584f9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'listcharacteristics', 'employercharacteristics', ['characteristic_uuid'], ['uuid'])
    op.create_foreign_key(None, 'listcharacteristics', 'company', ['company_uuid'], ['uuid'])
    op.add_column('listfieldactivities', sa.Column('field_activity_uuid', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'listfieldactivities', 'fieldactivity', ['field_activity_uuid'], ['uuid'])
    op.create_foreign_key(None, 'listfieldactivities', 'company', ['company_uuid'], ['uuid'])
    op.drop_column('listfieldactivities', 'activity_uuid')
    op.add_column('listhiringproblems', sa.Column('hiring_problems_uuid', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'listhiringproblems', 'hiringproblems', ['hiring_problems_uuid'], ['uuid'])
    op.create_foreign_key(None, 'listhiringproblems', 'company', ['company_uuid'], ['uuid'])
    op.drop_column('listhiringproblems', 'problem_uuid')
    op.create_foreign_key(None, 'listjobprofile', 'jobsprofile', ['job_profile_uuid'], ['uuid'])
    op.create_foreign_key(None, 'listjobprofile', 'company', ['company_uuid'], ['uuid'])
    op.create_foreign_key(None, 'listpreviouslyjobs', 'students', ['student_uuid'], ['uuid'])
    op.create_foreign_key(None, 'listpreviouslyjobs', 'previouslyjob', ['prev_job_uuid'], ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'listpreviouslyjobs', type_='foreignkey')
    op.drop_constraint(None, 'listpreviouslyjobs', type_='foreignkey')
    op.drop_constraint(None, 'listjobprofile', type_='foreignkey')
    op.drop_constraint(None, 'listjobprofile', type_='foreignkey')
    op.add_column('listhiringproblems', sa.Column('problem_uuid', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'listhiringproblems', type_='foreignkey')
    op.drop_constraint(None, 'listhiringproblems', type_='foreignkey')
    op.drop_column('listhiringproblems', 'hiring_problems_uuid')
    op.add_column('listfieldactivities', sa.Column('activity_uuid', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'listfieldactivities', type_='foreignkey')
    op.drop_constraint(None, 'listfieldactivities', type_='foreignkey')
    op.drop_column('listfieldactivities', 'field_activity_uuid')
    op.drop_constraint(None, 'listcharacteristics', type_='foreignkey')
    op.drop_constraint(None, 'listcharacteristics', type_='foreignkey')
    # ### end Alembic commands ###
