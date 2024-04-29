from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from . import crud, models, schemas
from .database import SessionLocal, engine

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
        raise HTTPException(status_code=404, detail="User not found")
    return db_student


@app.post("/students/", response_model=schemas.StudentReadReturn)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.put("/students/{stu_id}", response_model=schemas.StudentReadReturn)
def update_student(stu_id: int,student: schemas.StudentEdit, db:Session = Depends(get_db)):
    db_student = crud.get_student(db, stu_id = stu_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.edit_student(db = db, student=student)
    
@app.delete("/students/{stu_id}", response_model=schemas.StudentReadReturn)
def delete_student(stu_id: int,student: schemas.StudentDelete, db:Session = Depends(get_db)):
    db_student = crud.get_student(db, stu_id = stu_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.remove_student(db, stu_id=stu_id)


# Course

