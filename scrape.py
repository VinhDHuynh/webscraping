from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def get_html():
    url ="https://webscraper.io/test-sites/e-commerce/allinone"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def get_ratings(soup, cards):
    # find all pg tags with a data-rating attribute
    ratings_html = soup.find_all("p", {"data-rating" : re.compile(r".*")}) 
    ratings = []
    for rating in ratings_html:
        ratings.append(rating["data-rating"])
    return ratings

def get_costs(soup, cards):
    costs_html = soup.find_all("h4", {"class" : "price float-end card-title pull-right"})
    costs = []
    for cost in costs_html:
        costs.append(cost.string)
    return costs

def get_names(soup, cards):
    names_html = soup.find_all("a", {"class" : "title"})
    names = []
    for name in names_html:
        names.append(name["title"])
    return names

def main():
    html = get_html()
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all("div", {"class":"product-wrapper card-body"})
    ratings = get_ratings(soup, cards)
    costs = get_costs(soup, cards)
    names = get_names(soup, cards)
    print(names)
    
if __name__ == "__main__":
    main()
