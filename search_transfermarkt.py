from bs4 import BeautifulSoup
import requests, re
from unidecode import unidecode

base_url="https://www.transfermarkt.pl"
search_url = "/schnellsuche/ergebnis/schnellsuche?query="
footballer = input("Podaj nazwisko zawodnika:") 
print(f"Szukam zawodnika: {footballer}")


headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

response = requests.get(base_url + search_url + footballer.replace(" ", "+"), headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    pattern = re.compile(fr'\b\w*\s*{re.escape(footballer)}\b', re.IGNORECASE | re.UNICODE)
    results = soup.find_all('a', string=pattern)
    if len(results) > 0:
        print(f"Search results for '{footballer}':")
        for result in results:
            player_name = result.get_text()
            player_link = result['href']
            print(f"{player_name}: {base_url}{player_link}")
    else:
        print(f"No results found for '{footballer}'.")
        
