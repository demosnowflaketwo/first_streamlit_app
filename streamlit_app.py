import streamlit as st
st.title('🥣 My healthy Diner')
st.header('🥗Breakfast menu')
st.text('🐔pancakes & oatmeal')
st.text('🥑poriage')
st.text(' 🍞banna waffle')


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set the index of the table to be the fruit name and not the number
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

import requests
st.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json()) # this just writes the data on the screen

# normalize the json data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as a table 
st.dataframe(fruityvice_normalized)
