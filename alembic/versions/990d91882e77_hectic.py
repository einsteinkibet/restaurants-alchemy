"""hectic

Revision ID: 990d91882e77
Revises: d1e02286b6fc
Create Date: 2023-12-15 14:26:56.226717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '990d91882e77'
down_revision: Union[str, None] = 'd1e02286b6fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
