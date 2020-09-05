from functions import webtoonDownloader


url = "https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=910&weekday=mon"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Lanaguage": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}

webtoonDownloader(url, headers)
