from fastapi import APIRouter,Depends,HTTPException
from app.schema.schemas import PostSchema
from app.dependence import get_db
from app.models.user import User

postsRoute=APIRouter(prefix="/api/posts")

@postsRoute.post("{user_id}")
def get_posts(user_id:str,data:PostSchema,db=Depends(get_db)):
    user=db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user.posts