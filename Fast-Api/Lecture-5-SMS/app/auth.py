from passlib.context import CryptContext
import jwt
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.dependence import get_db
from app.models.user import User
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRE_TIME = os.getenv("EXPIRE_TIME")

session = HTTPBearer()

crypt_context = CryptContext(schemes=["argon2"], deprecated="auto")


def make_hash(pwd: str) -> str:
    return crypt_context.hash(pwd)


def verify_hash(pwd: str, hash_pwd: str) -> bool:

    return crypt_context.verify(pwd, hash_pwd)


def create_access_token(data: dict):
    payload = data.copy()
    expiry_time = datetime.now(timezone.utc) + timedelta(minutes=int(EXPIRE_TIME))
    payload["exp"] = expiry_time

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return token


def get_current_user(
    db=Depends(get_db), cred: HTTPAuthorizationCredentials = Depends(session)
) -> User:
    token = cred.credentials

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        user = db.get(User, data["id"])

        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")


class RoleChecker():
    def __init__(self, allowed_user: list[str]):
        self.allowed_user = allowed_user
   
    def __call__(self,user:User=Depends(get_current_user))->User:
        
        intersection=list()