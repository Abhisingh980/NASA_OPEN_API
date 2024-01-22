import random

import streamlit as st
import requests

api_key = "hGt8BaH71NS6NypV0TfpGJIUW1knHZCPqTPiMl0H"

url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={api_key}"

request = requests.get(url)

data = request.json()

#print(data)
for i in range(1, 1000):
    img = data['photos'][i]['img_src']
    st.image(img)


