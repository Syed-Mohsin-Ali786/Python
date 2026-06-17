from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database import Base



class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(String(50))

    posts:Mapped[list["Post"]]=relationship(
        back_populates="category"
    )