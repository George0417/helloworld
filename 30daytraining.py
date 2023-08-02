import streamlit as st
from datetime import time, datetime

st.header('Hi George')
st.write('It is a good day today :sunglasses:')

st.header('st.slider')
st.subheader('slider')

age=st.slider('How old are you', 0, 100, 5)
st.write('I'm', age, 'years old')
