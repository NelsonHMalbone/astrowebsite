import streamlit as sT
import config
import requests

apiKey = config.api_key
url = f'https://api.nasa.gov/planetary/apod?api_key={apiKey}'
response = requests.get(url)

content = response.json()

web_title = sT.title(content['title'])
