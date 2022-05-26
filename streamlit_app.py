import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text ('Idly with peanut chutney')
streamlit.text ('Vada with Sambar')
streamlit.text ('Upma and chutney')
streamlit.header ('Build your own Fruit Smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)
