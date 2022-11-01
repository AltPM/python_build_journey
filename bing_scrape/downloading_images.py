import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.domain.com.au/sale/pyrmont-nsw-2009/?excludeunderoffer=1")

souped = BeautifulSoup(page.content, "html.parser")
print(souped)  