
import streamlit as st
from datetime import time, datetime

st.header('Hi George')
st.write('It is a good day today :sunglasses:')


st.markdown('DAY 8')
st.header('st.slider')
st.subheader('slider')

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
