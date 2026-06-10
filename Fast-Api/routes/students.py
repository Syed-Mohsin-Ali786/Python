from fastapi import APIRouter
from util.helper import read, write

router = APIRouter(prefix="/student")

router.post("/post")


def student(data: dict):
    new_data = read()
    if new_data != []:
        for s in new_data:
            if s["id"] == data["id"]:
                return {"message": "already exist"}
        new_data.append(data)
    else:
        new_data = [data]

    write(new_data)
    return {"message": "successfully added"}


router.get("/api/get")


def students_data():
    return {"data": read()}


router.put("/put/{id}")


def update(id: int, data: dict):
    students = read()
    for index, student in enumerate(students):
        if student["id"] == id:
            students[index] = data
            write(students)
            return {"message": "successfully updated"}
    return {"message": "Not Found"}


router.delete("/delete/{id}")


def delete(id: int):
    students = read()
    new_students = [s for s in students if s["id"] != id]
    if len(new_students) == len(students):
        return {"message": "Not found"}
    write(new_students)
    return {"message": "successfully deleted"}
