from fastapi import APIRouter, Depends, HTTPException
from app.schema.schemas import PostSchema
from app.dependence import get_db
from app.models.post import Post

postsRoute = APIRouter(prefix="/api/posts", tags=["Posts"])


@postsRoute.post("/{user_id}")
def get_posts(data: PostSchema, db=Depends(get_db)):
    # user = db.get(User, data.user_id)
    # if not user:
    #     raise HTTPException(status_code=404, detail="user not found")
    post = Post(**data.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post
