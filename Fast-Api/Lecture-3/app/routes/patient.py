from fastapi import APIRouter
from models.patient import Patient
patient_router=APIRouter(prefix="/api/patient",tags=["Patient"])

@patient_router.post("")
def save(patient:Patient):
    return patient