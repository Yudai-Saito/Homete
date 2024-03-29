"""empty message

Revision ID: ef909c73f214
Revises: 1fa0f03b28b8
Create Date: 2022-12-21 21:32:14.226304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef909c73f214'
down_revision = '1fa0f03b28b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report_posts',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='fk_report_posts_post_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_report_posts_user_id'),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.add_column('posts', sa.Column('approved', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'approved')
    op.drop_table('report_posts')
    # ### end Alembic commands ###
