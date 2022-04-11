from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel as BaseSchema
from pydantic import Field


class Event(BaseSchema):
    message: str
    
    event_id: UUID = Field(default_factory=uuid4)

    timestamp: datetime = Field(default_factory=datetime.now)