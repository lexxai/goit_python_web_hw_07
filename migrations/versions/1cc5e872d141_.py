"""empty message

Revision ID: 1cc5e872d141
Revises: 5639e675f51f
Create Date: 2023-09-30 23:42:10.953576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cc5e872d141'
down_revision: Union[str, None] = '5639e675f51f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
