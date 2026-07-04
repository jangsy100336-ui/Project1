import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# 배경색 및 글자색 설정
st.markdown("""
<style>
.stApp {
    background-color: #001f5c;
    color: white;
}

h1, h2, h3, p, div {
    color: white !important;
}

div.stButton > button {
    background-color: white;
    color: #001f5c;
    border-radius: 10px;
    padding: 0.6em 1.5em;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #d9e6ff;
    color: #001f5c;
}
</style>
""", unsafe_allow_html=True)

# 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "home"

# 메인 화면
if st.session_state.page == "home":
    st.markdown(
        "<h1 style='text-align:center;'>👋 안녕하세요ㅎㅎ(≧▽≦*)</h1>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("나도 인사하기", use_container_width=True):
            st.session_state.page = "congrats"
            st.rerun()

# 축하 화면
else:
    st.balloons()

    st.markdown(
        "<h2 style='text-align:center;'>🎉 첫 웹페이지 제작을 축하해요!</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("돌아가기", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
