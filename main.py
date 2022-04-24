"""
main.py でやりたいこと
スクレイピングする各サイトに対して更新があるか確認。(この時点でもスクレイピングする)
あれば記事を取得して、apiにPOST
なければそのまま終了。
"""
from datetime import datetime, timedelta
from scraping import scrape_page
from parse_object import parse_kpopmonster
from typing import List
from send_mail import send_mail


def get_data(url, group_name, parser):
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
    # スクレイピングして記事を取得&整形する。
    articles = scrape_page(url, parser, group_name)

    print(articles)
    return articles


# 記事の重複をなくす
def deduplicate(results: List[dict]) -> List[dict]:
    filterd_results_all = []
    article_title_set = set()
    for result in results:
        if not result['title'] in article_title_set:
            filterd_results_all.append(result)
            article_title_set.add(result['title'])
        else:
            for filterd_dic in filterd_results_all:
                if filterd_dic['title'] == result['title']:
                    filterd_dic['group'].append(result['group'][0])
                    filterd_dic['group_id'].append(result['group_id'][0])

    return filterd_results_all


def main(url):
    description = 'default message'
    try:
        groups = ['blackpink', 'aespa', 'ive', 'gi-dle', 'kep1er', 'nmixx']
        results = []
        for group in groups:
            group_url = f'{url}?tag={group}'
            result: List[dict] = get_data(group_url, group, parse_kpopmonster)
            if len(result) > 0:
                results.append(*result)

        print(results)

        # 同記事複数グループのタグがあることがあるので、それもフィルタリングする。
        filterd_results = deduplicate(results)
        description = 'success!'

        # APIに送信する。

    except Exception as e:
        description = e

    # 結果をメールで送信
    # send_mail(title='scraping result', description=description)


if __name__ == '__main__':
    url = 'https://www.kpopmonster.jp/'
    main(url)


"""
herokuがインシデントを起こしたので、これからのスクレイピング＋定期実行の不具合への対処、対策
・ heroku → aws lambdaに移行
・ 障害発生時に取得できなかった記事を取得しmonogodbにinsertするプログラムを書く。
    不具合の旨を記載したメールかLINEを自分に送信。
    手動でスクレイピング、アップロード ← このプログラムを書くのが優先。(日付指定で取得できればいいかな。)
    
    
コレを機会にmongodbとDjangoを連携させるかなぁ。。。。→ やめました
    mongodbへの接続をサポートしてるdjongoの動作がよくわからない。
"""
