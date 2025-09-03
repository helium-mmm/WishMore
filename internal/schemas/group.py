from pydantic import BaseModel

class NewGroupRequest(BaseModel):
    name: str
    description: str
    closed: bool
    
class GroupResponse(BaseModel):
    id: int
    name: str
    description: str
    closed: bool
    password: str
    
    class Config:
        from_attributes = True