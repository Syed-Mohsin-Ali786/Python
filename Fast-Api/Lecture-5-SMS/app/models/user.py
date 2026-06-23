from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import Text, String, Enum as sqlEnum
from app.database import Base
from enum import Enum


class UserRole(str, Enum):
    admin = ("admin",)
    student = ("student",)
    teacher = "teacher"


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = MappedColumn(primary_key=True)

    name: Mapped[str] = MappedColumn(String(50))
    email: Mapped[str] = MappedColumn(String(50), unique=True)
    password: Mapped[str] = MappedColumn(Text)
    # role: Mapped[UserRole] = MappedColumn(sqlEnum(UserRole))
    roles: Mapped[list["Role"]] = relationship(
        secondary="user_roles", back_populates="users"
    )

    @property
    def role_name(self):
        return {role.name for role in self.roles}

    @property
    def permission(self):
        return {permission.name for role in self.roles for permission in role.permissions}
