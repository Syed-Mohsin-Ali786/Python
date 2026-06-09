from fastapi import FastAPI
from helper import write, read

app = FastAPI()


@app.get("/")
def home():
    return {"data": read()}


@app.post("/api/student")
def student(data: dict):
    write(data)
    return {"message": "successfully added"}


@app.get("/api/student")
def students_data():
    return {"data": read()}


@app.put("/api/student/{id}")
def update(id: int, data: dict):
    students = read()
    for index, student in enumerate(students):
        if student["id"] == id:
            students[index] = data
            break
    write(students)
    return {"message": "successfully updated"}


@app.delete("/api/student/{id}")
def delete(id: int):
    return {"id": id}
