# Logic to get the wanted matches

# Scrape player, FTU, pistol and flash data from https://www.hltv.org/stats
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.hltv.org/stats/players/")
soup = BeautifulSoup(response.text, 'html.parser')
for player in soup.find('table', attrs={"class":"stats-table player-ratings-table"}).find('tbody').find_all('tr'):
    print(player.find('a').text)
    print(player.find_all('td', class_='statsDetail' )[-1].text)
    print(player.find('td', class_='ratingCol' ).text)
    print('')

# Logic to calculate the winner
