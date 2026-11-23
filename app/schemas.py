from pydantic import BaseModel, Field, EmailStr

class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr

class StudentOut(StudentCreate):
    id: int