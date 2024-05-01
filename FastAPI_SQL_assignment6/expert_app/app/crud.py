from sqlalchemy.orm import Session

#from . import models, schemas
import schemas, models

# students

def get_student(db: Session, stu_id: int):
    return db.query(models.Student).filter(models.Student.id == stu_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db:Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def edit_student(db:Session, stu_id:int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == stu_id).first()
    if db_student is None:
        return False
    else:
        db_student = models.Student(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

def remove_student(db:Session, stu_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == stu_id).first()
    if db_student is None:
        return False
    else:
        db.delete(db_student)
        db.commit()
        #db.refresh(db_student)
        return True



# courses

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_student_course(db:Session, course: schemas.CourseCreate, stu_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == stu_id).first()
    if db_student is None:
        return False
    else:
        db_course = models.Course(**course.model_dump(), owner_id = stu_id)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
    return db_course

def edit_student_course(db: Session, course: schemas.CourseCreate, stu_id: int, course_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == stu_id).first()
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if (db_student is None) or (db_course is None):
        return False
    else:
        db_course = models.Course(**course.model_dump())
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return db_course

def remove_student_course(db: Session, course_id: int, stu_id:int):
    db_student = db.query(models.Student).filter(models.Student.id == stu_id).first()
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if (db_student is None) or (db_course is None):
        return False
    else:
        db.delete(db_course)
        db.commit()
        #db.refresh(db_course)
        return True
