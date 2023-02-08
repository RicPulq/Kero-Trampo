"""altera Int para Float

Revision ID: cb1e3a2fdcf5
Revises: e1c7e4a709a6
Create Date: 2023-02-08 15:14:08.127068

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "cb1e3a2fdcf5"
down_revision = "e1c7e4a709a6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "courses",
        "employability_index",
        existing_type=postgresql.INTEGER(),
        type_=postgresql.FLOAT(),
        nullable=False,
    )
    op.alter_column(
        "courses",
        "businessperson_index",
        existing_type=postgresql.INTEGER(),
        type_=postgresql.FLOAT(),
        nullable=False,
    )
    op.alter_column(
        "courses",
        "public_server_index",
        existing_type=postgresql.INTEGER(),
        type_=postgresql.FLOAT(),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "courses",
        "employability_index",
        existing_type=postgresql.FLOAT(),
        type_=postgresql.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "courses",
        "businessperson_index",
        existing_type=postgresql.FLOAT(),
        type_=postgresql.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "courses",
        "public_server_index",
        existing_type=postgresql.FLOAT(),
        type_=postgresql.INTEGER(),
        nullable=False,
    )
    # ### end Alembic commands ###
