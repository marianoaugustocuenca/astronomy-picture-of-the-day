import streamlit as st
import requests
import datetime

st.set_page_config(layout='wide')

fecha = datetime.date.today()
api_key = 'g6arSF6BhmOpSMO2EkxTZbuIAckYuh6WFwkbNNZh'
url = 'https://api.nasa.gov/planetary/apod?' \
      f'api_key={api_key}'

request = requests.get(url)


content = request.json()
st.title(content['title'])
response = requests.get(content['url'])

with open('image.jpg', 'wb') as file:
    file.write(response.content)

st.image('image.jpg')
st.write(content['explanation'])
