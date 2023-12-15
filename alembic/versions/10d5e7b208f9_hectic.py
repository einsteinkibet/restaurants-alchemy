"""hectic

Revision ID: 10d5e7b208f9
Revises: b4417322336d
Create Date: 2023-12-15 14:06:38.778760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10d5e7b208f9'
down_revision: Union[str, None] = 'b4417322336d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
