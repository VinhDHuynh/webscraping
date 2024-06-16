from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def get_html():
    url ="https://webscraper.io/test-sites/e-commerce/allinone"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def get_ratings(soup,cards):
    # find all pg tags with a data-rating attribute
    ratings_html = soup.find_all("p", {"data-rating" : re.compile(r".*")}) 
    ratings = []
    for x in ratings_html:
        ratings.append(x["data-rating"])
    return ratings
# h4 class="price float-end card-title pull-right" for costs
def main():
    html = get_html()
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all("div", {"class":"product-wrapper card-body"})
    ratings = get_ratings(soup, cards)


if __name__ == "__main__":
    main()
