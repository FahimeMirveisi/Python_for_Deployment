from sqlalchemy.orm import Session

from . import models, schemas

# students

def get_student(db: Session, user_id: int):
    return db.query(models.Student).filter(models.Student.id == user_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db:Session, student: schemas.StudentCreate):
    
# courses

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


