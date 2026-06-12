from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    url="sqlite:///database.db", connect_arg={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=True,
    autocommit=False
    )

Base=declarative_base()