"""hectic

Revision ID: d1e02286b6fc
Revises: c646c7a0b709
Create Date: 2023-12-15 14:19:47.891858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1e02286b6fc'
down_revision: Union[str, None] = 'c646c7a0b709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
