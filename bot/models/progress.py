from typing import Optional
from pydantic import BaseModel


class Progress(BaseModel):
    name: str
    surname: str
    mark: Optional[int]

    def __str__ (self):
        return f'{self.name} {self.surname}: {self.mark if self.mark else "Не оценено"}\n'


class ProgressEnumerated(Progress):
    id: int

    def __str__(self):
        return f': <code>{self.id}</code>: ' + super().__str__()

