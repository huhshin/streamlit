import streamlit as st
import pandas as pd

st.markdown('# Unit 1. Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')

# title, header, subheader, caption
st.markdown('## 1. Title, Header, Subheader, Caption')

st.title('this is the title')
st.header('this is the header')
st.subheader('this is the subheader')
st.text('this is the text')
st.caption('Caption in small font')

# Markdown 
# st.markdown('## 2. Markdown')

# st.markdown('# This is a Markdown title')
# st.markdown('## This is a Markdown header')
# st.markdown('### This is a Markdown subheader')
# st.markdown('This is the markdown')
# st.markdown('This is **the markdown 진하게**')
# st.markdown('This is _the markdown 기울임_')
# st.markdown('This is **_the markdown 진하고 기울임_** ')

# st.markdown('- item 1\n'
#             '   - item 1.1\n'
#             '   - item 1.2\n'
#             '      - item 1.2.1\n'
#             '- item 2')

# st.markdown('1. item 1\n'
#             '   1. item 1.1\n'
#             '   2. item 1.2\n'
#             '      1. item 1.2.1\n'
#             '2. item 2')

# code, latex-수학식 표현
# st.markdown('## 3. Code, Latex')

# st.code('x=2021')
# st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right) ''') 

# st.write
# String, data_frame, chart, graph, LaTex 등의 objects를 App에  출력할 수 있다.
# st.markdown('## 4. Write')
# st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')

# st.write('this is a string write')
# st.write('Hello, *World!* 😎')

# df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text_lec.py