# Get the weather and rain of brazilian cities
# Imports
import requests
from bs4 import BeautifulSoup
import os
import unidecode

def clean_text(dirty_city_name):
    # Clean the city name
    # unidecode to remove accents
    city = unidecode.unidecode(dirty_city_name).lower()
    city = city.replace(' ', '-')
    return city

def get_weather(city):
    # Get the weather and rain percentage
    # Counter
    i = 0
    # Make and go to url
    url = f'https://www.tempo.com/{city}.htm'
    page = requests.get(url)

    # Html page to BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    texts = soup.find_all('div')

    # Find the informations
    for text in texts:   
        if text.get_text().count('Sensação Térmica') == 1:
            dirty_text = text.get_text().split(' ')

            # Get weather and rain values
            for word in dirty_text:
                if word == 'Chuva':
                    rain = dirty_text[i+2]
                elif word == 'Térmica':
                    weather = dirty_text[i+2]
                i += 1

            # Clean prompt
            os.system('cls')

            # Print informations
            return print(
                f'Cidade: {city}\n',
                f'Temperatura: {weather}°C\n',
                f'Probabilidade de chuva: {rain}')

city_name = ''       
while city_name != 'exit':
    print("type 'exit' to exit")
    city_name = input('Cidade: ')
    clean_city_name = clean_text(city_name)
    get_weather(clean_city_name)

#get_weather(clean_text(input('Cidade: ')))

