from fastapi import FastAPI
from helper import  read
from routes.students import router as std_router
router = FastAPI(
   prefix="/api" 
)


@router.get("/")
def home():
    return {"data": 'this is the home page'}


