import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Company webpage")

content = """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Pellentesque sapien. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos. 
Nullam justo enim, consectetuer nec, ullamcorper ac, vestibulum in, elit. In convallis. 
Duis bibendum, lectus ut viverra rhoncus, dolor nunc faucibus libero, eget facilisis enim ipsum id lacus. 
Suspendisse nisl. Nullam justo enim, consectetuer nec, ullamcorper ac, vestibulum in, elit. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content)

st.header("Our Team")

df = pandas.read_csv("data.csv", sep=",")
topics = pandas.read_csv("topics.csv")
print(topics)

col1, space1, col2, space2, col3 = st.columns([1, 0.5, 1, 0.5, 1])
# col1, col2, col3 = streamlit.columns(3)

with col1:
    for index, row in df[0:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")
