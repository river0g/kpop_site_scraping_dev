from pydantic import BaseModel
from typing import Optional


class Article(BaseModel):
    title: str
    detail: str
    url: str
    thumbnail: str
    date: str
    datetime: int
    author: str
    group: list
    group_id: list
    source_site: str
    source_site_id: str
