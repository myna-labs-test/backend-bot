from typing import List, Dict, Type
from datetime import datetime
from pydantic import BaseModel


def format_records_enumerated(raw_models: List[Dict[str,str]], model: Type[BaseModel]) -> list[BaseModel]:
    if not raw_models:
        return []
    return list(map(lambda p: model(**p[1],position=p[0]), enumerate(raw_models)))


def format_date(date: str) -> str:
    return datetime.fromisoformat(date).strftime('%d.%m.%y %H:%M')