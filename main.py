import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("data.csv")
st.markdown('<span style="color:red">College Student Data Analytics</span>',unsafe_allow_html=True)
st.markdown('<span style="color:yellow font-size:50px">ADIT Student Data</span>',unsafe_allow_html=True)


if st.sidebar.button("load dataset"):
    st.write(df)
if st.sidebar.button("show graph"):
    df2=df.head()
    fig=plt.figure(figsize=(15,10))
    plt.bar(df2['sl'],df2["Trade"])
    st.pyplot(fig)
if st.sidebar.button("scatter plot"):
    df2=df.head()
    fig=plt.figure(figsize=(15,10))
    plt.scatter(df2['sl'],df2["Trade"])
    plt.xlabel("sl",fontsize=15)
    plt.ylabel("Trade",fontsize=15)
    st.pyplot(fig)
if st.sidebar.button("show data"):
    df3=df.sample()
    st.write(df3)
if st.sidebar.button("Contact us"):
    st.image("download.jpg")
    st.markdown('<span style="color:yellow font-size:50px">ADIT Student Data</span>',unsafe_allow_html=True)
    
  

    
