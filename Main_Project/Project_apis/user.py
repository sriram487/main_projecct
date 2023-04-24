import time

from sqlalchemy import Table, Column, Integer, String, Date
from sqlalchemy.orm import registry

mapper_registry = registry()

user_table = Table(
    "data",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("date", Date),
    Column("time", String(20)),
)


class User:
    pass


mapper_registry.map_imperatively(User, user_table)
