from pydantic import BaseModel
from enum import Enum


class SenderType(str, Enum):
    USER: str = 'USER'
    CHARACTER: str = 'CHARACTER'


class MessageNew(BaseModel):
    sender_type: SenderType
    message: str
    character_id: str
    tg_id: int
