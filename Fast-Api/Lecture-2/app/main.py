from fastapi import FastAPI
from router.product import pd_router
app = FastAPI(prefix="/api")


app.include_router(pd_router)