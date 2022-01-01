import pandas as pd
import streamlit as st

data = {
  'Series_1': [1, 2, 3, 4, 7],
  'Series_2': [10, 30, 40 ,100, 250]
}

df = pd.DataFrame(data)

st.title('Our first Streamlit App')
st.subheader('Introducing Streamlit in Automate Everythin with Python')
st.write('''This is our first Web App.
Enjoy it!''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)