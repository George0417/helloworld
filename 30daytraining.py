
import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np
from streamlit_pandas_profiling import st_profile_report


st.header('Hi George')
st.write('It is a good day today :sunglasses:')

st.subheader('DAY 8 st.slider')

st.markdown('#Example1')
age=st.slider('How old are you', 0, 100, 5)
st.write("I'm", age, 'years old')

st.markdown('#Example2')
st.subheader('Range slider')
values=st.slider('select a range of value', 0.0,100.0,(25.0,75.0))
st.write('values:',values)

st.markdown('#Example3')
st.subheader('Range time slider')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.markdown('#Example4')
st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


st.subheader('DAY 9 st.line_chart')

chart_data=pd.DataFrame(
  np.random.randn(20,3),
  columns=['a','b','c']
)

st.line_chart(chart_data)


st.subheader('DAY 10 st.selectbox')
option=st.selectbox(
  'how many kids do you have?',
  ('1','2','3','4')
)
st.write('your kids number is ', option)


st.subheader('Day11 st.multiselect')
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'])

st.write('You selected:', options)


st.subheader('Day12 st.checkbox')
st.write('what would you like to order?')

icecream=st.checkbox('ICE CREAM')
coffee=st.checkbox('coffee')
cola=st.checkbox('cola')

if icecream:
  st.write("Great! Here's some more 🍦")

if coffee:
  st.write("Okay, here's some coffee ☕")

if cola:
  st.write("Here you go 🥤")


st.subheader('Day14 component')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)
