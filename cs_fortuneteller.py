import requests
from bs4 import BeautifulSoup
# Logic to get the wanted matches

response = requests.get("https://www.hltv.org/matches")
soup = BeautifulSoup(response.text, 'html.parser')
# let's first get the next match
teams = []
for match in soup.find(attrs={"class":"upcomingMatchesSection"}).find(attrs={"class":"upcomingMatch"}).find_all(attrs={"class":"matchTeamName"}):
    teams.append(match.text)
print(f"The match between: {teams} Will be estimated")

# Get team compositions
team1 = []
team2 = []


# Get team stats


# Scrape player, FTU, pistol and flash data from https://www.hltv.org/stats
'''
response = requests.get("https://www.hltv.org/stats/players/")
soup = BeautifulSoup(response.text, 'html.parser')
for player in soup.find('table', attrs={"class":"stats-table player-ratings-table"}).find('tbody').find_all('tr'):
    print(player.find('a').text)
    print(player.find_all('td', class_='statsDetail' )[-1].text)
    print(player.find('td', class_='ratingCol' ).text)
    print('')
'''

# Logic to calculate the winner
