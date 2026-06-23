from fastapi import FastAPI
from app.models.user import User
from app.database import Base, engine
from app.routers.authentication import router as auth_router
from app.models.role import Permission,Role
app = FastAPI()
app.include_router(auth_router)

Base.metadata.create_all(engine)
