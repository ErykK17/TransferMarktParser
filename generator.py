import random as r
import requests
from bs4 import BeautifulSoup

def la_masia_generator(names,surnames):
    names_list = []
    surnames_list = []
    with open(names, encoding="utf8") as names_file:
        for line in names_file:
            names_list.append(line.strip('\n'))
    with open(surnames, encoding="utf8") as surnames_file:
        for line in surnames_file:
            surnames_list.append(line.strip('\n').lower().capitalize())
    
    return f"{names_list[r.randrange(len(names_list))]} {surnames_list[r.randrange(len(surnames_list))]}"

base_url="https://www.transfermarkt.pl"
search_url = "/schnellsuche/ergebnis/schnellsuche?query="
phrase = la_masia_generator("names.txt", "surnames.txt")

print(base_url + search_url + phrase.replace(" ","+"))

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
response = requests.get(base_url + search_url + phrase.replace(" ","+"), headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'parser.html')
    results = soup.find_all('a', string=phrase)
    if len(results) > 0:
        print(f"Search results for '{phrase}':")
        for result in results:
            player_name = result.get_text()
            player_link = result['href']
            print(f"{player_name}: {base_url}{player_link}")
    else:
        print(f"No results found for '{phrase}'.")
        
def test():
    pass
