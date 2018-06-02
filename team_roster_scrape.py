import requests
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime

team = input("Who is your favorite team? ").lower()
year = datetime.now().year

response = requests.get(f"https://www.nba.com/{team}/roster/{year}")
soup = BeautifulSoup(response.text, "html.parser")
players = soup.find_all(class_="roster__player__header")

with open(f"{team}_roster.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["name", "position", "jersey_number"])
    for player in players:
        name = player.find(class_="roster__player__header__heading").text
        position = player.find(class_="roster__player__header_position").text
        jersey_number = player.find(class_="roster__player__header_jnumber").text
        csv_writer.writerow([name,position,jersey_number])
# data = soup.find_all(class_="roster__player__header__heading")
# print(f"Here is the current roster for the {team} \n")
# for player in data:
#     print(f"{player.text} \n")