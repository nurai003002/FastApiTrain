from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP,JSON, ForeignKey, Boolean
from datetime import datetime

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registred_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=True, nullable=False)
)
