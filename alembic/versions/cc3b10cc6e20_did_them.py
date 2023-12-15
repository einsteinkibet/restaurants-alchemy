"""did them

Revision ID: cc3b10cc6e20
Revises: 31e8d2e976dc
Create Date: 2023-12-15 13:11:57.356163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc3b10cc6e20'
down_revision: Union[str, None] = '31e8d2e976dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
