from pydantic import BaseModel
from enum import Enum
from uuid import UUID


class MessageNew(BaseModel):
    sender_type: str
    message: str
    character_id: UUID
    tg_id: int


class MessageShort(BaseModel):
    text: str
    character_id: UUID