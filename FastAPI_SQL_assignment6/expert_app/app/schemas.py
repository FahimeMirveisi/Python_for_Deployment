from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    unit: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id:int
    owner_id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    firstname: str
    lastname: str
    average: float | None
    graduated: bool
    

class StudentCreate(StudentBase):
    name: str
    unit: int

class Student(StudentBase):
    id: int
    courses: list[Course] = []

    class Config:
        orm_mode = True