import jwt
from datetime import datetime,timezone,timedelta
SECRET_KEY="SYD-256"
ALGORITHM="HS256"
EXPIRE_TIME=30

def create_access_token(data:dict):
    payload=data.copy()
    expiry_time=datetime.now(timezone.utc)+timedelta(
        minutes=EXPIRE_TIME
    )
    payload["exp"]=expiry_time

    token=jwt.encode(
        SECRET_KEY,
        payload,
        algorithm=ALGORITHM,
    )
    return token