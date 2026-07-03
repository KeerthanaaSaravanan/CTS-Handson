"""create student table

Revision ID: 79845e102082
Revises: 98b0916968eb
Create Date: 2026-07-01 21:41:11.533773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79845e102082'
down_revision: Union[str, None] = '98b0916968eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
