from sqlalchemy.orm import Session

from . import models, schemas

# students

def get_student(db: Session, stu_id: int):
    return db.query(models.Student).filter(models.Student.id == stu_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db:Session, student: schemas.StudentCreate):
    db_student = models.Student(firstname = student.firstname, lastname = student.lastname,
                                 average = student.average, graduated = student.graduated)
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def edit_student(db:Session, student: schemas.StudentEdit):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def remove_student(db:Session, student: schemas.StudentDelete, stu_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == stu_id).first()
    db.delete(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message": "student with {stu_id} deleted"}



# courses

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_student_course(db:Session, course: schemas.CourseCreate, stu_id: int):
    db_course = models.Course(**course.model_dump(), owner_id = stu_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def edit_student_course(db: Session, course: schemas.CourseEdit, stu_id: int):
    pass

def remove_student_course(db: Session, course: schemas.CourseDelete, stu_id:int):
    pass
