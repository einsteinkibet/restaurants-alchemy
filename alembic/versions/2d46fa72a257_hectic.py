"""hectic

Revision ID: 2d46fa72a257
Revises: 45258de729d4
Create Date: 2023-12-15 14:34:03.262972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d46fa72a257'
down_revision: Union[str, None] = '45258de729d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
