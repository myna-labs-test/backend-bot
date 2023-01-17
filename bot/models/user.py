from pydantic import BaseModel


class UserFull(BaseModel):
    first_name: str
    last_name: str
    username: str
    tg_id: int


class UserShort(BaseModel):
    tg_id: int