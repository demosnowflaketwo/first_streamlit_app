import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

st.title('🥣 My healthy Diner')
st.header('🥗Breakfast menu')
st.text('🐔pancakes & oatmeal')
st.text('🥑poriage')
st.text(' 🍞banna waffle')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set the index of the table to be the fruit name and not the number
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)


#crete function
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    # st.text(fruityvice_response.json()) # this just writes the data on the screen
    # normalize the json data 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # output as a table 
    st.write('thank you for adding', this_fruit_choice)
    return fruityvice_normalized

st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
      st.error("pleasse select a fruit to get information")
  else:
      back_from_func= get_fruitvice_data(fruit_choice)
      st.dataframe(back_from_func)
except:
  st.error()

st.header("view our fruit list - add your favorites")

#  snowflake - related functions:
def  get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
#  add a button to load the fruit
if st.button('Get fruit list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    st.dataframe(my_data_rows)

# st.stop()
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
        return "thanks for adding " + new_fruit

add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_func = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    st.text(back_from_func)

