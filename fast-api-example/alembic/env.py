import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, create_engine, exc, text
from sqlalchemy import pool

from alembic import context

from storage.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def create_db_if_not_exists():
    db_uri = os.getenv('POSTGRESQL')
    database = db_uri.split('/')[-1]
    db_postgres = "/".join(db_uri.split('/')[0:-1])+"/postgres"
    try:
        engine = create_engine(db_uri)
        with engine.connect() as conn:
            print(f'Database {database} already exists.')
    except exc.OperationalError:
        print(f'Database {database} does not exist. Creating now.')
        engine = create_engine(db_postgres)
        with engine.connect() as conn:
            conn.execute(text("commit"))
            conn.execute(text(f'CREATE DATABASE {database};'))


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    create_db_if_not_exists()

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


config.set_main_option('sqlalchemy.url', os.getenv("POSTGRESQL"))

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


