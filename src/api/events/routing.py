from fastapi import APIRouter
from .schema import EventSchema


router = APIRouter()

@router.get("/")
def read_events():
    return {
        "items": [1,2,3]
    }

@router.get("/{event_id}")
def event(event_id: int) -> EventSchema :
    """ 
        give data of a specific event.
        Args:
            event_id (int): the id of the event.
        Returns:
            dict: the data of the event. 
    """
    return {
        "id": event_id
    }