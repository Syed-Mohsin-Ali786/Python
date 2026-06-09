from fastapi import FastAPI
from helper import write, read

app = FastAPI()


@app.get("/")
def home():
    return {"data": read()}


@app.post("/api/student")
def student(data: dict):
    new_data=read()
    if new_data!=[]:
        for s in new_data:
            if s["id"]==data["id"]:
                return {"message": "already exist"}
        new_data.append(data)
    else:
        new_data=[data]
    
    write(new_data)
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
            write(students)
            return {"message": "successfully updated"}
    return {"message": "Not Found"}


@app.delete("/api/student/{id}")
def delete(id: int):
    students = read()
    new_students=[s for s in students if s["id"]!=id]
    if len(new_students)==len(students):
        return {
            "message":"Not found"
        }
    write(new_students)
    return {"message": "successfully deleted"}
