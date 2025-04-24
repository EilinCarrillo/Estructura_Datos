from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    name: str 
    type: str 
    identity: str 
    case_description: str 
    age: int 
    priority_attention: bool 
    priority: Optional[int] = None  
