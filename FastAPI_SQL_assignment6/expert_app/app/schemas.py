from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    unit: int

class CourseCreate(CourseBase):
    pass




class StudentBase(BaseModel):
    firstname: str
    lastname: str
    average: float
    graduated: bool
    