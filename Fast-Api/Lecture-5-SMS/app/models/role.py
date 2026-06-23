from sqlalchemy.orm import Mapped,relationship
from sqlalchemy import Table,Column,ForeignKey
from app.database import Base

class Role(Base):
    id:Mapped[int]
    name:Mapped[str]
    permissions:Mapped[list["Permission"]]=relationship(
        secondary="role_permissions",
        back_populates="roles"
    )
    users:Mapped[list["User"]]=relationship(
        secondary="user_role",
        back_populates="roles"
    )

class Permission(Base):
    __tablename__="permissions"
    id:Mapped[int]
    name:Mapped[str]

# pivot table
role_permissions=Table(
    "role_permissions",Base.metadata,
    Column("permission_id",ForeignKey("permissions.id",ondelete="cascade"),primary_key=True),
    Column("role_id",ForeignKey("roles.id",ondelete="cascade"),primary_key=True)
)

user_roles=Table(
    "user_role",Base.metadata,
    Column("user_id",ForeignKey("users.id",ondelete="cascade"),primary_key=True),
    Column("role_id",ForeignKey("roles.id",ondelete="cascade"),primary_key=True)
)