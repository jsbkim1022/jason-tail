import requests
import json
import os
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
from io import BytesIO


url = "https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=910&weekday=mon"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Lanaguage": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}
res = requests.get(url, headers=headers)
html = res.text
soup = BeautifulSoup(html, "lxml")


def webtoonNameFinder():
    # webtoon Name finding
    webtoonName = soup.find_all("h3")
    episodename = webtoonName[0].get_text()


# Webtoon Download
cartoons = soup.find_all("img", attrs={"alt": "comic content"})

imagelinks = []
for cartoon in cartoons:
    link = cartoon.get("src")
    imagelinks.append(link)
print(f"found {len(imagelinks)} images for the episode {episodename}")

# webtoon downloading


def webtoonDownloader(episodename, imagelinks, headers):
    try:
        os.mkdir("%s" % episodename)
    except:
        None

    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink, headers=headers)
        img_data = response.content
        image_bytes = BytesIO(img_data)
        img = Image.open(image_bytes)
        img.save("%s/.%s.jpg" % (episodename, i))


webtoonDownloader(episodename, imagelinks, headers)

# # example
# img_url = "https://image-comic.pstatic.net/webtoon/675554/910/20191024201714_df8d818df0e9a4a79106a5ed6f21c7e5_IMAG01_14.jpg"
# response = requests.get(img_url, headers=headers)
# img_data = response.content
# image_bytes = BytesIO(img_data)
# img = Image.open(image_bytes)
# img.save("first.jpg")

# automatic scarpping for one episode
