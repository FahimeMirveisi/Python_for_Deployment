from pydantic import BaseModel


#**********Course**********

# Base(Parent class for Course)
class CourseBase(BaseModel):
    name: str
    unit: int

# Create
class CourseCreate(CourseBase):
    pass

# Read and return
class Course(CourseBase):
    id:int
    owner_id: int

    class Config:
        #orm_mode = True
        from_attributes = True

#**********Student**********

#Base(Parent class for Student)
class StudentBase(BaseModel):
    firstname: str
    lastname: str
    average: float | None
    graduated: bool
    
# Create
class StudentCreate(StudentBase):
    pass

# Read
class Student(StudentBase):
    id: int
    courses: list[Course] = []

    class Config:
        #orm_mode = True
        from_attributes = True
