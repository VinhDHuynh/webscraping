from urllib.request import urlopen
url ="https://webscraper.io/test-sites/e-commerce/allinone"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
