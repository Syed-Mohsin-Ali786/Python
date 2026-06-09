from fastapi import FastAPI
from helper import write

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hi"}


@app.post("/api/student")
def student(data: dict):
    write(data)
    return {"message": "successfully added"}


@app.get("/api/student")
def students_data(data: dict):
    return {"data": data}


@app.put("/api/student/{id}")
def update(id: int):
    return {"update": id}


@app.delete("/api/student/{id}")
def delete(id: int):
    return {"id": id}
