import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)




with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Ong Kit Wei")
    content =  """
            Hi, i am Ardit! I am a python programmer,, teacher and founder of PythonHow. I graduated in 2013 with a master of science in Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote sensing. I have worked with companies from various countries, such as the Center for COnservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
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




