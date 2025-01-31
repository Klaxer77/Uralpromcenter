"""initial

Revision ID: 1f268e6bf748
Revises: c0e3c33dff96
Create Date: 2024-09-16 18:07:07.791311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f268e6bf748'
down_revision: Union[str, None] = 'c0e3c33dff96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'progress', ['img'])
    op.create_unique_constraint(None, 'recall', ['img'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recall', type_='unique')
    op.drop_constraint(None, 'progress', type_='unique')
    # ### end Alembic commands ###
