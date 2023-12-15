"""weuuh

Revision ID: 9f0b3b73feca
Revises: 3947ec3a64f6
Create Date: 2023-12-15 13:49:40.426991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f0b3b73feca'
down_revision: Union[str, None] = '3947ec3a64f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
