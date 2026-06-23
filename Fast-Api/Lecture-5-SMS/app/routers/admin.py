from fastapi import APIRouter, Depends, HTTPException
from app.schemas.userSchema import UserRegisterSchema
from app.auth import check_access_token,RoleChecker
from app.dependence import get_db
from app.models.user import User

router = APIRouter(prefix="/admin")


@router.post("/teacher")
def get_teacher_data(user:User=Depends(RoleChecker(["teacher"])))->User:
   user
    if not data:
        raise HTTPException(status_code=204, detail="No content found")
    return {"teachers": data}
