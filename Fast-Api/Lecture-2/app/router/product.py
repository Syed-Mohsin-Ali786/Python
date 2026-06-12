from fastapi import APIRouter

pd_router = APIRouter(prefix="/product")


@pd_router.get("/")
def get_product(arg):
    return {"message": "this is product page"}
