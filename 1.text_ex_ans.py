# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# title, header, subheader, caption 
st.markdown('# Unit 1. 연습문제- Text elements ')

st.markdown('## 1. Header, Subheader, Text, Caption')
st.markdown('- **_header 연습_**')
st.header('Header: 데이터 분석 표현')
st.markdown('- **_subheader 연습_**')
st.subheader('Subheader: 스트림릿')
st.markdown('- **_text 연습_**')
st.text('Text: this is the Streamlit')
st.markdown('- **_caption 연습_**')
st.caption('Caption: Streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹어플리케이션 툴이다')

# code, latex-수학식 표현
st.markdown('## 2. Code, Latex')
st.latex(r''' a + ar + ar^2 + ar^3  ''') 
st.code('a + ar + ar^2 + ar^3')

# write 작성하기
# 아래 딕셔너리를 데이터 프레임으로 변경
# {'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}
st.markdown('## 3. Write')
df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})
st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서', df, '스트림릿의 write 함수로 표현')
