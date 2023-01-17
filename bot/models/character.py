from pydantic import BaseModel
from uuid import UUID


class Character(BaseModel):
    id: UUID
    name: str
    position: int

    def __str__(self):
        return f'<code>{self.position}</code>: {self.name}'


class CharacterChange(BaseModel):
    character_id: UUID
    tg_id: int


class CharacterShort(BaseModel):
    character_id: UUID


class CharacterTextResponse(BaseModel):
    text: str