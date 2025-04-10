import streamlit as st

st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="centered")


st.title("Welcome to my python website.")


st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Home","About","Contact"])


if page == "Home":
    st.header("Home Page")
    st.write("This is simple and beautiful Homepage built with streamlit and python..")
    name = st.text_input("What\'s your name? ")
    if name:
        st.success(f"Hello {name}! Thanks for visiting!!")




elif page == "About":
    st.header("About Page")
    st.write("This is simple and beautiful Aboutpage built with streamlit and python..")
    


if page == "Contact":
    st.header("Contact Page")
    email = st.text_input("Your email ")
    message = st.text_input("Your message ")
    if st.button("Submit"):
        st.success("Thank you we have recieved your message")

