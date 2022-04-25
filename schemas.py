from pathlib import Path
from pydantic import BaseModel, parse_obj_as, ValidationError
from typing import Optional, List


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


class Member(BaseModel):
    name: str
    age: int


if __name__ == '__main__':
    jfile = None
    with open('./test.json', 'r') as f:
        import json
        jfile = f.read()
        jfile = json.loads(jfile)

    # print(jfile)

    try:
        # apiでjsonをやり取りする時にList[dict]の形式に対応したスキーマ
        members = parse_obj_as(List[Member], jfile)
        print("members: ", members)
        print("members[3]: ", members[3].json())

    except ValidationError as e:
        print(e.json())
