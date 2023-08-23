import streamlit as st
import pandas

with st.sidebar:
    st.write("Home")
    st.write("Contact me")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Ong Kit Wei")
    content =  """
            Hi, i am kit wei a graduate EEE student from Singapore Polytechnic (SP).
            My interest lies in robotics and i spent my 6 months internship in a Autonomus 
            Vehicle(AV) company working as a Test Engineer.
                """
    st.info(content)

content2 = """
            Below you can find some of the apps i have built in Python. Feel free to contact me!
            """    
st.write(content2)


col3, empty_col, col4 = st.columns([1.5,0.5,1.5])


data = pandas.read_csv("data.csv",sep=";")
for index, row in data[:10].iterrows():
    with col3:
        st.title(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

for index, row in data[10:].iterrows():
    with col4:
        st.title(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")




