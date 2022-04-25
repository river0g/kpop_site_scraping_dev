from typing import List
import requests
from decouple import config
from settings import api_username, api_password
import json


def get_jwt_token() -> str:
    url = 'http://localhost:8001/api/jwttoken'

    body = {
        'username': api_username,
        'password': api_password
    }
    res = requests.post(url, data=json.dumps(body))
    res = res.json()
    token = res['token']
    return token


# print(get_jwt_token())


def post_data(data: List[dict]):
    url = 'http://localhost:8001/api/article'

    token = get_jwt_token()

    headers = {
        'authorization': f'JWT {token}'
    }

    res = requests.post(url, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    # data = [{'title': 'Kep1erのパフォーマンス中に突然Stray Kidsの曲が登場！？ 「VENOMが始まるのかと思った」・・ 『QUEENDOM2』での予想外の出来事にビックリ', 'detail': '『QUEENDOM2』 第4話のKep1erのパフォーマンス中に、Stray Kidsの「VENOM」のイントロのような音が聞こえると話題になっている。 3月31日から放送が開始されている、Mnet主催のK-POPガール…', 'url': 'https://www.kpopmonster.jp/?p=108587', 'thumbnail': 'https://www.kpopmonster.jp/wp-content/uploads/2022/04/kep1er-stray-kids01-486x290.jpg', 'date': '2022.04.25', 'datetime': 1650812400, 'author': '14tk', 'group': ['kep1er'], 'group_id': ['005'], 'article_id': 'a108587', 'source_site': 'kpopmonster', 'source_site_id': 'a'},
    #         {'title': 'Kep1er、『QUEENDOM2』でダヨン＆チェヒョンがステージから転落・・ ハプニング続きの彼女たちにヒカルがかけた言葉に感動！ 18歳とは思えない大人な考えに称賛の声続出', 'detail': '『QUEENDOM2』 第4話で、Kep1erが数々のハプニングに見舞われてしまう。落ち込むメンバーたちをなぐさめるヒカルの言葉にも注目が集まっている。 日中韓合同のオーディション番組 『Girls Planet 999…', 'url': 'https://www.kpopmonster.jp/?p=108498', 'thumbnail': 'https://www.kpopmonster.jp/wp-content/uploads/2022/04/kep1er04-5-486x290.jpg', 'date': '2022.04.25', 'datetime': 1650812400, 'author': '14tk', 'group': ['kep1er'], 'group_id': ['005'], 'article_id': 'a108498', 'source_site': 'kpopmonster', 'source_site_id': 'a'}]

    # post_data(data)

    url = 'http://localhost:8001/api/article'
    token = get_jwt_token()

    headers = {
        'authorization': f'JWT {token}'
    }

    res = requests.get(url, headers=headers)
    print(res.json())
