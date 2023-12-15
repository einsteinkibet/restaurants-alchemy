"""hectic

Revision ID: b650f9bb9492
Revises: 10d5e7b208f9
Create Date: 2023-12-15 14:09:54.920759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b650f9bb9492'
down_revision: Union[str, None] = '10d5e7b208f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
