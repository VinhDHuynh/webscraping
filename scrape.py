from bs4 import BeautifulSoup
from urllib.request import urlopen

def retrieve_html():
    url ="https://webscraper.io/test-sites/e-commerce/allinone"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def main():
    html = retrieve_html()
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all("div", {"class":"product-wrapper card-body"})
    print(cards)


if __name__ == "__main__":
    main()
