from typing import List
from group_map import group_id
from datetime import datetime, timedelta
from time_trans import dateTime2unixTime


def parse_kpopmonster(soup, group_name) -> List[dict]:
    """Soupオブジェクトをdictに変換する。対象サイトはkpopmonster。

    Parameters
    ----------
    soup : beautifulsoup object ( bs4.element.Tag )
        解析対象のsoupオブジェクト
    group_name : str
        返却するdictのgroupキーの値として固定するためにある。

    Returns
    -------
    articles : List[dict]
    """
    articles_soup = soup.find_all('article', class_='post-list')

    def inner(article) -> dict:
        article_title = article.section.h1.text.replace('\n', '')
        article_detail = article.find(
            'div', class_='description').text.replace('\n', '')
        article_detail_url = article.a['href']
        article_thumbnail_url = article.img['src']
        article_date = article.section.find('span', class_='date').text
        article_author = article.find(
            'p', class_='entry-meta').find('span', class_='author').text

        article_id = article_detail_url.replace(
            'https://www.kpopmonster.jp/?p=', '')
        article_id = "a" + str(article_id)

        year = int(article_date[:4])
        mon = int(article_date[5:7])
        day = int(article_date[8:])
        article_datetime = dateTime2unixTime(year, mon, day)

        # 今日のデータのみを取得するためのフィルターに使うもの
        now_date = datetime.now()
        yesterday = now_date - timedelta(1)
        yesterday: str = yesterday.strftime('%Y.%m.%d')
        # # yesterday = '2021.03.13'  # aespa と blackpinkのみ
        # yesterday = '2021.11.01'  # 3groupあり

        # 昨日の記事がない場合はNoneを返す。
        if yesterday != article_date:
            return None

        parsed_data = create_dict(
            article_title,
            article_detail,
            article_detail_url,
            article_thumbnail_url,
            article_date,
            article_datetime,
            article_author,
            [group_name],
            [group_id(group_name)],
            article_id,
            'kpopmonster',
            'a'
        )

        return parsed_data

    articles = list(map(inner, articles_soup))

    # 上記のinnerでNoneしか返されなかった時に空の配列として返すためのもの
    def filter_func(article):
        if article:
            return article

    articles = list(filter(filter_func, articles))

    return articles


def parse_kstyle(soup, group_name):
    """Soupオブジェクトをdictに変換する。対象サイトはkstyle。

    Parameters
    ----------
    soup : beautifulsoup object ( bs4.element.Tag )
        解析対象のsoupオブジェクト
    group_name : str
        返却するdictのgroupキーの値として固定するためにある。

    Returns
    -------
    articles : List[dict]
    """
    pass


def create_dict(title, detail, url, thumbnail, date, datetime, author, group, group_id, article_id, source_site, source_site_id):
    return {
        "title": title,
        "detail": detail,
        "url": url,
        "thumbnail": thumbnail,
        "date": date,
        "datetime": datetime,
        "author": author,
        "group": group,
        "group_id": group_id,
        "article_id": article_id,
        "source_site": source_site,
        "source_site_id": source_site_id,
    }
