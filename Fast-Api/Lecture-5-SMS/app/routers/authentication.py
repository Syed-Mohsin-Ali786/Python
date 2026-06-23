from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.userSchema import UserRegisterSchema, LoginSchema
from app.dependence import get_db
from app.models.user import User
from sqlalchemy.exc import IntegrityError
from app.auth import verify_hash, create_access_token, check_access_token, make_hash,RoleChecker


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register_post(data: UserRegisterSchema, db=Depends(get_db)):
    try:
        user = User(
            name=data.name,
            email=data.email,
            password=make_hash(data.password),
            role=data.role,
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        db.rollback()  # Always rollback the session after a database error

        # Check if it's specifically a duplicate entry error (MySQL error code 1062)
        if "1062" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists.",
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database integrity violation.",
        )


@router.post("/login")
def login(data: LoginSchema, db=Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="invalid email")
    if not verify_hash(data.password, user.password):
        raise HTTPException(status_code=401, detail="invalid password")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "Bearer"}


@router.get("/profile")
def profile(user = Depends(RoleC    hecker(["admin","student"]))):
    return user
    
