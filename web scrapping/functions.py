import requests
import json
import os
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
from io import BytesIO


def webtoonDownloader(url, headers):

    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")

    h3 = soup.find_all("h3")
    episodename = h3[0].get_text()

    cartoons = soup.find_all("img", attrs={"alt": "comic content"})
    imagelinks = []
    for cartoon in cartoons:
        link = cartoon.get("src")
        imagelinks.append(link)
    print(f"From url, we found {len(imagelinks)} images for the episode {episodename}")

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
    print("%s images have been saved at %s folder" % (len(imagelinks), episodename))
