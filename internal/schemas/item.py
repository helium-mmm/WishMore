from pydantic import BaseModel

class NewItemRequest(BaseModel):
    name: str
    description: str
    count: int
    cost: float 
    img: str
    group_id: int
    
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    count: int
    cost: float 
    img: str
    group_id: int
    
    class Config:
        from_attributes = True