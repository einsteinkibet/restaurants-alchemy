"""did them

Revision ID: 3947ec3a64f6
Revises: 072d1b900106
Create Date: 2023-12-15 13:43:20.618183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3947ec3a64f6'
down_revision: Union[str, None] = '072d1b900106'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
