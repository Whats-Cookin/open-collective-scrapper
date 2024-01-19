from bs4 import BeautifulSoup
import requests

from ..lib.pipe import clean_img_url_for_slug

url_to_scrape = "https://discover.opencollective.com/"

def get_org_slug():
    get_data = requests.get(url_to_scrape)
    soup = BeautifulSoup(get_data.text, "html.parser")

    img_urls = soup.findAll("img", attrs={"class":"Table__Avatar-sc-fu01nh-1"})

    for url in img_urls:
        clean_img_url_for_slug(url)
