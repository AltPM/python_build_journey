from collections import Counter
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import os
from decouple import config
from dotenv import load_dotenv
load_dotenv()


subscription_key = config('subscrtiption_key', default='')
# print(os.getenv("subscription_key"))

search_url = "https://api.bing.microsoft.com/v7.0/search"
search_term = 'Does nike have a sweatshop in vietnam?'
subscription_key='3a1ca0f8f2aa4cf999088a0128675593'
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

pages = search_results['webPages']
# pprint(pages)
results = pages['value']


print(search_results.keys())
pages = search_results['webPages']
pprint(pages.keys()) # value key is more valuble
results = pages['value']
# pprint(results[0])
# pprint(pages)

for result in results[:10]:
    response = requests.get(result['url'])
    # content = response.content
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(content)
    text = soup.find('body').get_text().strip()
    cleaned_text = ' '.join(text.split('\n'))
    cleaned_text = ' '.join(text.split())
    counter = Counter([x for x in cleaned_text.split() if len(x) > 10])
    print(counter.most_common(10))
    # print(text)
    print(cleaned_text)
    break


