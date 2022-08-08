# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

st.title('Unit 3. Data display elements')

st.header(' 1. Metric')
# metric 코드 작성하기
st.metric(label='Temperature', value='30.5 °C', delta='2.5 °C')
st.metric(label='Temperature', value='28 °C', delta='-2.5 °C')

st.header('2. columns')
# columns 코드 작성하기
col1, col2, col3 = st.columns(3)
col1.metric('기온', '30.5 °C', '2.5 °C')
col2.metric('풍속', '9 mph', '-8%')
col3.metric('습도', '86%', '4%')

st.header('3. Dataframe')
# titanic csv 파일 위치- https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv
titanic = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv')
st.dataframe(titanic)

st.header('4. Table')
# table 코드 작성하기
st.table (titanic)
