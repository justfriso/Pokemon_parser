from bs4 import BeautifulSoup
import requests

url = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'

"""
writing a program to determine what types are most common, what type combos
do not yet exist and what types are most common in which region using the
current(februari 2024) pokedex from "https://www.serebii.net/pokemon/nationalpokedex.shtml"
"""

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

pokemon_attributes = soup.find_all('td', class_="fooinfo")

with open('pokemon_attributes.txt', 'w', encoding='utf-8') as file:
    print("Pokemon Attributes:", file=file)
    for attribute in pokemon_attributes:
        print(attribute.text, file=file)


with open('pokemon_attributes.txt', 'r') as file:
    lines = file.readlines()


for line in lines:
    print(line.strip()) 
