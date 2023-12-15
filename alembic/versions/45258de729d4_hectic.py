"""hectic

Revision ID: 45258de729d4
Revises: 990d91882e77
Create Date: 2023-12-15 14:32:05.258715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45258de729d4'
down_revision: Union[str, None] = '990d91882e77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
