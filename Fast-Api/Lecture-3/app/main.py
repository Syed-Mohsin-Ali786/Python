from fastapi import FastAPI
from routes.patient import patient_router
app=FastAPI()

app.include_router(patient_router)