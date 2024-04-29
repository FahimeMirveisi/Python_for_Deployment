from pydantic import BaseModel


#**********Course**********

# Base(Parent class for Course)
class CourseBase(BaseModel):
    name: str
    unit: int

# Create
class CourseCreate(CourseBase):
    pass

# Read
class CourseReadReturn(CourseBase):
    id:int
    owner_id: int

    class Config:
        #orm_mode = True
        from_attributes = True
# Update
class CourseEdit(CourseBase):
    id: int
    owner_id: int

# Delete
class CourseDelete(CourseBase):
    id: int
    owner_id: int

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
class StudentReadReturn(StudentBase):
    id: int
    courses: list[CourseReadReturn] = []

    class Config:
        #orm_mode = True
        from_attributes = True

# Update
class StudentEdit(StudentBase):
    id: int
    courses: list[CourseReadReturn] = []

# Delete
class StudentDelete(StudentBase):
    id: int
    courses: list[CourseReadReturn] = []