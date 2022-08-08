# streamlit, pandas 라이브러리 불러오기 
import streamlit as st

# title로 'Unit 2. Media elements' 표시하기 
st.title('Unit 2. Media elements')

# image
# header로 '1. Image' 표시하기  
st.header("1. Image")
# 이미지 코드 작성하기
# 이미지 주소 https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80
st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80', caption='산에서 본 해돋이')

# audio
# header로 '2. Audio' 표시하기 
st.header('2. Audio')
# 오디오 코드 작성하기- 2.MusicSample.mp3
st.audio('2.MusicSample.mp3')  

# video 
# header로 '3. Video' 표시하기
st.header('3. Video')
# 비디오 코드 작성하기- 2.VideoSample.mp4
st.video('2.VideoSample.mp4')
