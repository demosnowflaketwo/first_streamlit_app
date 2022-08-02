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
st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])

# Display the table on the page.
st.dataframe(my_fruit_list)
