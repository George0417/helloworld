import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np


st.subheader('DAY 10 st.selectbox')
option=st.selectbox(
  'how many kids do you have?',
  ('1','2','3','4')
)
st.write('your kids number is ', option)


st.subheader('Day11 st.multiselect')
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

