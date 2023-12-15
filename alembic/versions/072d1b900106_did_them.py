"""did them

Revision ID: 072d1b900106
Revises: cc3b10cc6e20
Create Date: 2023-12-15 13:22:26.678316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '072d1b900106'
down_revision: Union[str, None] = 'cc3b10cc6e20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
