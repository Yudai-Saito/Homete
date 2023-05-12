"""empty message

Revision ID: 1fa0f03b28b8
Revises: 5de21e093929
Create Date: 2022-12-01 09:37:32.624784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fa0f03b28b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reaction', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('reaction')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.Column('contents', sa.String(length=400), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('head', sa.String(length=15), nullable=True),
    sa.Column('face', sa.String(length=15), nullable=True),
    sa.Column('facialhair', sa.String(length=15), nullable=True),
    sa.Column('accessories', sa.String(length=15), nullable=True),
    sa.Column('skincolor', sa.String(length=15), nullable=True),
    sa.Column('clothingcolor', sa.String(length=15), nullable=True),
    sa.Column('haircolor', sa.String(length=15), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_posts_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_reactions',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('reaction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='fk_post_reactions_posts_id'),
    sa.ForeignKeyConstraint(['reaction_id'], ['reactions.id'], name='fk_post_reactions_reaction_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_post_reactions_user_id'),
    sa.PrimaryKeyConstraint('user_id', 'post_id', 'reaction_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_reactions')
    op.drop_table('posts')
    op.drop_table('users')
    op.drop_table('reactions')
    # ### end Alembic commands ###
