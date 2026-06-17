from fastapi import APIRouter, Depends
from app.schemas.userSchema import UserRegisterSchema
from app.dependence import get_db
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/")
def register_post(data: UserRegisterSchema, db=Depends(get_db)):
    user = User(name=data.name, email=data.email, password=data.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
