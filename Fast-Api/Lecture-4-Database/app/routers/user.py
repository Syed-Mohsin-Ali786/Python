from fastapi import APIRouter, Depends, HTTPException
from app.dependence import get_db
from app.models.user import User
from app.schema.schemas import UserSchema

router = APIRouter(prefix="/api/user")


@router.get("")
def get_users(db=Depends(get_db)):
    data = db.query(User).all()
    return data


@router.post("")
def add_user(request: UserSchema, db=Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=422, detail="This email already exists")

    new_user = User(name=request.name, email=request.email)
    db.add(new_user)
    db.commit()
    return {"successfully added"}