このプロジェクトの目的: 特定のサイトから自分のみたいものだけ取得してサイトに表示する。

# 主要機能

スクレイピングと API(fastapi)を通して mongodb に POST。\
kpop_site_api、kpop_site_frontend と連携する。

todo: コードを整理する。\
todo: API と連携する。\
todo: 取得サイトの拡張。 \
TODO: 上記プログラムが終了したら LINE に通知を送る。

# スクレイピング

対象のサイトから記事のタイトル、詳細、記事の内容、画像の URL を取得する。\
使ったもの: requests, beautifulsoup\
ファイル: scraping.py,

# 対象サイト

- k-popmonster
- Kstyle
- more...
