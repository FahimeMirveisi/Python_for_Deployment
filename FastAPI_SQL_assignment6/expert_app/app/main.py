from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from . import crud, models, schemas
#import crud, schemas, models

from .database import SessionLocal, engine
#from database import SessionLocal, engine

#import database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    msg = "Wellcome to my university application"
    return msg

# Student

@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.get("/students/{stu_id}", response_model=schemas.Student)
def read_student(stu_id: int, db:Session = Depends(get_db)):
    db_student = crud.get_student(db, stu_id = stu_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.put("/students/{stu_id}", response_model=schemas.Student)
def update_student(stu_id: int,student: schemas.StudentCreate, db:Session = Depends(get_db)):
    db_student = crud.edit_student(db = db, stu_id=stu_id,student=student)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
    
@app.delete("/students/{stu_id}")
def delete_student(stu_id: int, db:Session = Depends(get_db)):
    db_student = crud.remove_student(db, stu_id=stu_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return "student with {stu_id} id deleted"


# Course

@app.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@app.post("/students/{stu_id}/courses", response_model=schemas.Course)
def create_student_course(stu_id: int,course: schemas.CourseCreate, db: Session = Depends(get_db)) :
    db_course = crud.create_student_course(db=db, course=course, stu_id=stu_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_course

@app.put("students/{stu_id}/courses/{course_id}", response_model=schemas.Course)
def update_student_course(stu_id: int, course_id: int, course:schemas.CourseCreate, db:Session = Depends(get_db)):
    db_course = crud.edit_student_course(db=db, course=course, stu_id=stu_id, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Student or course not found")
    return db_course

@app.delete("students/{stu_id}/courses/{course_id}")
def delete_student_course(stu_id: int, course_id: int, db:Session = Depends(get_db)):
    db_course = crud.remove_student_course(db, stu_id=stu_id, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Student or course  not found")
    
    return "Course with {course_id} id for student {stu_id} deleted."