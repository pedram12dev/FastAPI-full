from typing import List
from pydantic import BaseModel



class EventSchema(BaseModel):
    id: int


class EventListSchema(BaseModel):
    items: List[EventSchema]