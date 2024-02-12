"""
writing a program to determine what types are most common, what type combos
do not yet exist and what types are most common in which region using the
current(februari 2024) pokedex from "https://www.serebii.net/pokemon/nationalpokedex.shtml"
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

article_titles = soup.find_all('td', class_="fooinfo")

for title in article_titles:
    print(title.text)
