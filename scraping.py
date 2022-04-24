# scraping
from bs4 import BeautifulSoup as bs4
import time
import lxml
import requests
import json
from typing import List


def scrape_page(url: str, parse_func, group_name: str) -> List[dict]:
    """引数に渡されたページをスクレイピングして個々の記事を解析してdictにしたあと、まとめてリストにする。

    Parameters
    ----------
    url : str
        スクレイピング対象のURL
    parse_func : callback function
        bs4オブジェクトをdictに変換する関数。
        なにも処理せずそのままbs4オブジェクトを返したいなら以下を引数にする。
        lambda soup: soup

    Returns
    -------
    aricles : List[dict]
    """

    res = requests.get(url)
    time.sleep(3)
    res.encoding = res.apparent_encoding
    html_doc = res.text
    soup = bs4(html_doc, "lxml")
    articles = parse_func(soup, group_name)

    return articles


# def data_dumps(parsed_data) -> str:
#     if type(parsed_data) == 'str':
#         return parsed_data
#     return json.dumps(parsed_data, ensure_ascii=False, indent=2)


# test用
if __name__ == '__main__':
    # url = page_url(1, 'blackpink')
    result = scrape_page('https://www.kpopmonster.jp/?tag=blackpink',
                         parse_overview_kpopmonster, "blackpink")
    print(result[0]['title'])
