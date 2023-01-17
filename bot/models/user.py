from pydantic import BaseModel, Field


class UserFull(BaseModel):
    first_name: str = Field(None)
    last_name: str = Field(None)
    username: str = Field(None)
    tg_id: int = Field(None)


class UserShort(BaseModel):
    tg_id: int