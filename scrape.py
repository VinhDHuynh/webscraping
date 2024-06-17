from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas as pd
import csv

csv_file_path = "./output.csv"

def get_html():
    url ="https://webscraper.io/test-sites/e-commerce/allinone"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html
    
def get_attributes(soup, cards, tag:str, key:str, value, desired_val:str, enclosed:bool=False) -> list:
    attrs_html = soup.find_all(tag, {key : value})
    attrs = []
    for attr in attrs_html:
        if enclosed:
            attrs.append(attr.string)
        else:
            attrs.append(attr[desired_val])    
    return attrs

def main():
    html = get_html()
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all("div", {"class":"product-wrapper card-body"})
    
    ratings = get_attributes(soup, cards, "p", "data-rating", re.compile(r".*"), "data-rating")
    costs = get_attributes(soup, cards, "h4", "class", "price float-end card-title pull-right", None, True)
    names = get_attributes(soup, cards,"a", "class", "title", "title")

    headers = ["Name", "Cost", "Rating"]
    with open("output.csv", 'w+') as file: 
        writer = csv.DictWriter(file, delimiter=',', fieldnames=headers) 
        writer.writeheader()
    
    df = pd.read_csv(csv_file_path)
    df["Name"] = names
    df["Cost"] = costs
    df["Rating"] = ratings
    df.to_csv(csv_file_path, index=False)
        
if __name__ == "__main__":
    main()
