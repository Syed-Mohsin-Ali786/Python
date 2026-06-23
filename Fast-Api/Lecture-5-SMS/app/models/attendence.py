from sqlalchemy.orm import Mapped,relationship
from sqlalchemy import Table,Column,ForeignKey
from app.database import Base


class Attendence(Base):
    