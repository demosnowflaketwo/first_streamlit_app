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
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('thank you for adding', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# st.text(fruityvice_response.json()) # this just writes the data on the screen
# normalize the json data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as a table 
st.dataframe(fruityvice_normalized)


import snowflake.connector
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit list containes:")
st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thank you for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('Amir')")

