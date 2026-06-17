from fastapi import FastAPI
from app.database import Base, engine
from app.routers.user import router as userRoute
from app.routers.posts import postsRoute
from app.models.user import User
from app.models.post import Post
from app.models.category import Category
app = FastAPI()
app.include_router(userRoute)
app.include_router(postsRoute)
Base.metadata.create_all(engine)

