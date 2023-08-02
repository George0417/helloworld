import streamlit as st
from datetime import time, datetime

st.header('Hi George')
st.write('It is a good day today :sunglasses:')

st.header('st.slider')
st.subheader('slider')

age=st.slider('How old are you', 0, 100, 5)
st.write("I'm", age, 'years old')

st.subheader('Range slider')

values=st.slider('select a range of value', 0.0,100.0,(25.0,75.0))
st.write('values:',values)
