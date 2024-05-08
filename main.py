import streamlit as sT
import config
import requests

sT.set_page_config(layout='wide')

apiKey = config.api_key
url = f'https://api.nasa.gov/planetary/apod?api_key={apiKey}'

# first response
response = requests.get(url)
content = response.json()

# extract url,explanation,title
title = content['title']
img_url = content['url']
explanation = content['explanation']

# secodary response for img download
img_path = 'img.png'
response2 = requests.get(img_url)
with open(img_path, 'wb') as file:
    file.write(response2.content)

# website
sT.title(title)
sT.image(img_url)
sT.write(explanation)
