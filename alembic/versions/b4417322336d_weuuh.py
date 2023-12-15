"""weuuh

Revision ID: b4417322336d
Revises: 9f0b3b73feca
Create Date: 2023-12-15 13:59:27.930030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4417322336d'
down_revision: Union[str, None] = '9f0b3b73feca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
