"""initial db setup

Revision ID: 5f0f3c4692eb
Revises: 
Create Date: 2020-06-26 01:14:38.432291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f0f3c4692eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('unit')
    op.drop_table('scenario')
    op.drop_table('origin')
    op.drop_table('demand')
    op.drop_table('vehicle')
    op.drop_table('stop')
    op.drop_table('asset_class')
    op.drop_table('model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('asset_class',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stop',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('scenario_id', sa.INTEGER(), nullable=False),
    sa.Column('vehicle_id', sa.INTEGER(), nullable=False),
    sa.Column('stop_num', sa.INTEGER(), nullable=False),
    sa.Column('stop_distance', sa.FLOAT(), nullable=False),
    sa.Column('unit_id', sa.INTEGER(), nullable=False),
    sa.Column('demand_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['demand_id'], ['demand.id'], ),
    sa.ForeignKeyConstraint(['scenario_id'], ['scenario.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('max_capacity_units', sa.FLOAT(), nullable=False),
    sa.Column('unit_id', sa.INTEGER(), nullable=False),
    sa.Column('asset_class_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['asset_class_id'], ['asset_class.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('demand',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('latitude', sa.FLOAT(), nullable=True),
    sa.Column('longitude', sa.FLOAT(), nullable=True),
    sa.Column('units', sa.FLOAT(), nullable=False),
    sa.Column('unit_id', sa.INTEGER(), nullable=False),
    sa.Column('cluster_id', sa.INTEGER(), nullable=True),
    sa.Column('model_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['model.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('origin',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('latitude', sa.FLOAT(), nullable=True),
    sa.Column('longitude', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scenario',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=16), nullable=True),
    sa.Column('model_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
