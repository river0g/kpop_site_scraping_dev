from random import randint
from datetime import datetime
import time


def dateTime2unixTime(year: int, mon: int, day: int, hour: int = 0, minute: int = 0, second: int = 0):
    """日付からUNIX時間を算出する。投稿時間が不明な場合は0時0分0秒とする。
    Parametersに合致しない日付の場合はエラーが起きる。(存在しない日付はエラーが起きる。)のでexceptで0を返す

    Parameters
    ----------
    year : int
        対象年を4桁で渡す。例: 2022
    mon : int
        対象月を2桁で渡す。1-12のintが対象。例: 12
    day : int
        対象日を2桁で渡す。1-31のintが対象。例: 21
    hour : int, default 0
        対象時間を2桁で渡す。1-23のintが対象。例: 12
    minute : int, default 0
        対象分を2桁で渡す。1-59のintが対象。例: 40
    second : int, default 0
        対象秒を2桁で渡す。1-59のintが対象。例: 57

    Returns
    -------
    u : int
        UNIX時間(10桁の数字)
    """
    try:
        d = datetime(year, mon, day, hour, minute, second)
        u = int(time.mktime(d.timetuple()))
        return u
    except:
        return 0


# output: 例 2022-04-01 00:00:00
def unixTime2dateTime(sec: int):
    """UNIX時間から日付を算出する。使う？？

    Parameters
    ----------
    sec : int
        UNIX時間(msの場合は1000で割る) 例: 

    Returns
    -------
    d : str
        日付の文字列を返却する。例: 2021-12-30 00:00:00
    """
    s = str(sec)
    if len(s) == 11 and int(s[0]) == 1:
        sec = int(sec / 10)
    if len(s) == 12:
        sec = int(sec / 100)
    if len(s) == 13 or int(s[0]) >= 2:
        sec = int(sec / 1000)
    d = str(datetime.fromtimestamp(sec))
    return d


if __name__ == '__main__':
    u = unixTime2dateTime(1640790000)
    print(dateTime2unixTime(2022, 4, 31))
