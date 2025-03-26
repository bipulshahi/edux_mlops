import streamlit as st

st.title('Streamlit demo')

st.header("Header on the top")

st.text("This is a example text")

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")

if st.checkbox("Select/Deselect"):
    st.text("Checkbox is selected")
else:
    st.text("Checkbox is not selected")

state = st.radio("What is your favorite color" , ("Red","Green","Yellow"))
if state == 'Green':
    st.success('Well that is my favorite too')

user_name = st.text_input('Enter your name')
user_age = st.number_input("Enter your age")