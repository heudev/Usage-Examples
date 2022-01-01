import requests
from bs4 import BeautifulSoup

site = requests.get("")
soup = BeautifulSoup(site.text, features="html.parser")
#soup = soup.prettify() (regular)

path = soup.select('table > tbody > tr > td:nth-child(2)')
tag = soup.find_all("tr")
tag_css = soup.find_all("td", attrs={"style": "width:236px"})

print(soup.text)
