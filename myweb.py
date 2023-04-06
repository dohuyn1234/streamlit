import streamlit as st

st.set_page_config(
    page_title="선택과목 사전조사",
    page_icon='🤔'
)

st.title(':red[**선택과목 과탐**] 사전 조사')

학년 = st.radio("귀하의 학년은 무엇입니까?", ('1학년', "2학년", "3학년"))

if 학년 == '1학년':
    st.write('1학년 전용 설문으로 이동하십시오.')
if 학년 == '2학년':
    st.write('승인 되었습니다')
if 학년 == '3학년':
    st.write('3학년 전용 설문으로 이동하십시오.')

반 = st.radio("귀하의 반은 무엇입니까?", ('1반', "2반", "3반", '4반', '5반', '6반', '7반', '8반', '9반'))

title = st.text_input('번호')
st.write('귀하의 학번은:', title)

options = st.multiselect(
    '탐구과목 선택 ( 해당과목 모두 선택가능 )',
    ['물리학1', '화학1', '생물학1', '지구과학1'],
)

st.write('선택된 과목:', options)

ori_id = "dohuyn123"
ori_pw = '1234'

id = st.sidebar.text_input('아이디')
pw = st.sidebar.text_input('비밀번호', type='password')
login = st.sidebar.button("로그인")

agree = st.sidebar.checkbox('로봇이 아닙니다')

if agree:
    st.sidebar.write('사진속 문자를 입력하세요')

    st.sidebar.image('robot.jpg', width=200)
    robot = st.sidebar.text_input('인증단어')

    if robot == "푸른밤":
        st.sidebar.write('인증성공!')
    else:
        st.sidebar.write('다시 시도하세요')

if login:
    if ori_id == id:



        if ori_pw == pw:
            st.header(id + '님 환영합니다.')
            st.sidebar.write('김도현')
            st.sidebar.image('프로필.jpg', width=300)
            st.sidebar.subheader(id)



        else:
            st.header('비밀번호가 일치하지 않습니다.')
    else:
        st.header(id + '아이디가 존재하지 않습니다.')


