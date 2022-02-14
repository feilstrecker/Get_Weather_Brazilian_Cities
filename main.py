# Imports
import requests
from bs4 import BeautifulSoup
import unidecode

def clean_text(dirty_city_name):
    # Clean the city name
    # unidecode to remove accents
    city = unidecode.unidecode(dirty_city_name).lower()
    city = city.replace(' ', '-')
    return city

def get_weather(city):
    # Get the weather and info about the day
    # Headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27'}
    # Make and go to url
    url = f'https://www.tempo.com/{city}.htm'
    page = requests.get(url, headers=headers)

    # Html page to BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the informations
    title = soup.find_all('h1', class_='titulo')[0]

    weather = soup.find_all('span', class_='dato-temperatura changeUnitT')[0]

    info = soup.find_all('span', class_='datos')[4]

    return print(
        f'{title.text}\n\n'
        f'Temperatura: {weather.text}\n',
        f'{info.text}'
    )

    

city_name = ''       
while city_name != 'exit':
    print("type 'exit' to exit")
    city_name = input('Cidade: ')
    clean_city_name = clean_text(city_name)
    get_weather(clean_city_name)

#get_weather(clean_text(input('Cidade: ')))

