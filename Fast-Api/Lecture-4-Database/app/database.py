from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    url="sqlite:///UserDatabase.db", connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=True,
    autocommit=False,
    bind=engine
    )

Base=declarative_base()
