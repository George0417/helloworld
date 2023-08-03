import streamlit as st
import pandas as pd
import numpy as np

st.header('HI george')
st.write('Have a good day! :sunglasses:')


st.subheader('DAY 9 st.line_chart')

chart_data=pd.DataFrame(
  np.random.randn(20,3),
  columns=['a','b','c']
)

st.lin_chart(chart_data)
