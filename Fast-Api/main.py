from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "hi"}


students = [{"id": 1, "name": "ali"}, {"id": 2, "name": "muh"}, {"id": 3, "name": "kazim"}]


@app.post("/api/student")
def add_student(data: dict):
    students.append(data)
    return {"message": "successfully added"}


@app.get("/api/student")
def students_data(data: dict):
    return {"data": data}


@app.put("/api/student/{id}")
def update(id: int,data:dict):
    for index, student in enumerate(students):
        if student["id"]==id:
            students[index]=data
    return {"update": id}


@app.delete("/api/student/{id}")
def delete(id: int):
    return {"id": id}
