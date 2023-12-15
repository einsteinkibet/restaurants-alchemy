"""hectic

Revision ID: c646c7a0b709
Revises: b650f9bb9492
Create Date: 2023-12-15 14:15:13.954984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c646c7a0b709'
down_revision: Union[str, None] = 'b650f9bb9492'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
