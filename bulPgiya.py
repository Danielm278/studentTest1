import streamlit as st

target = 123

st.title("ברוכים הבאים לבול פגיעה")
user = st.number_input("אנה תבחרו מספר")

if user == target:
    st.success("קלעת בול!")
