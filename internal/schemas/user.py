from pydantic import BaseModel, EmailStr

class UserRequest(BaseModel):
    email: EmailStr
    name: str
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    
    class Config:
        from_attributes = True