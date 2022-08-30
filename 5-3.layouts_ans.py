import streamlit as st
import pandas as pd

# 메인페이지 
# Iris 사진- https://ouellette001.com/PapiersPeints/images/Iris_versicolor_0021_1280.jpg
# data_iris.csv 출력하기 
def main_page():
    st.header('Main Page')
    st.image('https://ouellette001.com/PapiersPeints/images/Iris_versicolor_0021_1280.jpg', width=400)
    iris = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv')
    st.dataframe(iris)
    
# 2페이지: 세 개의 columns으로 나누어 꽃 이름과 사진 나타내기
def page2():
    st.header('Page 2')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg')
    with col2:
        st.text('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg')
    with col3:
        st.text('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg')

# 3페이지: 세 개의 tab을 사용하여 iris 3가지 꽃 나타내기
def page3():
    st.header('Page 3')
    tab1, tab2, tab3 = st.tabs(['Setosa', 'Versicolor', 'Virginica'])
    with tab1:
        st.header('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg', width=500)       
    with tab2:
        st.header('Versicolo')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg', width=500)      
    with tab3:
        st.header('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg', width=500)   

# 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }
page_names_to_funcs = {'Main Page': main_page, 'Page 2': page2, 'Page 3': page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-3.layouts_ans.py