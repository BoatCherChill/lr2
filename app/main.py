from fastapi import FastAPI, HTTPException
from app import schemas

app = FastAPI(title="LR2")

students = {}
next_id = 1

@app.post("/students", response_model=schemas.StudentOut, status_code=201)
def create_student(data: schemas.StudentCreate):
    global next_id
    for s in students.values():
        if s["email"] == data.email:
            raise HTTPException(400, "Студент с таким email уже есть")
    record = data.model_dump()
    record["id"] = next_id
    students[next_id] = record
    next_id += 1
    return record

@app.get("/students", response_model=list[schemas.StudentOut])
def list_students():
    return list(students.values())

@app.get("/students/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(404, "Студент не найден")
    return students[student_id]

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(404, "Студент не найден")
    del students[student_id]
    return None