"""add_column_address_uuid_table_Company

Revision ID: 2239ff61dd5f
Revises: 5946d3d454fb
Create Date: 2022-10-13 16:53:01.472868

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2239ff61dd5f'
down_revision = '5946d3d454fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('address_uuid', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'company', 'user', ['address_uuid'], ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'company', type_='foreignkey')
    op.drop_column('company', 'address_uuid')
    # ### end Alembic commands ###
