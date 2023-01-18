from pydantic import BaseModel, Field
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
    character_id: UUID = Field(None)


class CharacterText(BaseModel):
    text: str
    character_id: str
    text_driver: str
    tts_driver: str
    model_id: str


class CharacterTextResponse(BaseModel):
    text: str