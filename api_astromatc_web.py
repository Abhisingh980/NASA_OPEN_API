import streamlit as st
import requests

# API KEY
api_key = "hGt8BaH71NS6NypV0TfpGJIUW1knHZCPqTPiMl0H"

# URL LINK OF API
url = "https://api.nasa.gov/planetary/apod?\
api_key=hGt8BaH71NS6NypV0TfpGJIUW1knHZCPqTPiMl0H"

# request for url
response = requests.get(url)
data = response.json()
date = data['date']
title = data['title']
explanation = data['explanation']
image_url = data['hdurl']
image_url2 = data['url']

# creating image file for which save the image for further use
image_filepath = "image.png"
image = requests.get(image_url2)

with open(image_filepath, "wb") as file:
    # write content in file
    file.write(image.content)

# output in web page
st.header(title.title())
col1, col2 = st.columns(2)
with col1:
    st.image(image_url)
    st.write("Direct from link")
with col2:
    st.image(image_filepath)
    st.write("Download from link then write in file.png then load")

st.write(date)
st.write(explanation)
