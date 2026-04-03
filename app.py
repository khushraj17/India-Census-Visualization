import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="India Census Data Analysis", page_icon=":bar_chart:", layout="wide")
df = pd.read_csv("dataset/India.csv")
l = list(df['State'].unique())
l.insert(0,"Overall Analysis")


st.sidebar.title("India Census Data Analysis")
analysis_type = st.sidebar.selectbox("Select Analysis Type", ["Overall Analysis", "State Analysis"])
# btn1 = st.sidebar.button("submit")

if analysis_type == "Overall Analysis":
    primary_param = st.sidebar.selectbox("Select Primary Parameter", ["Population", "Male", "Female", "Literate"])
    secondary_param = st.sidebar.selectbox("Select Secondary Parameter", ["Population", "Male", "Female", "Literate"])

    fig = px.scatter_map(df,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="District",
                        size=primary_param,
                        color=secondary_param,  
                        map_style ="dark",
                        size_max=15, 
                        zoom=4,
                        color_discrete_sequence=["#00FFFF"])
    st.plotly_chart(fig)

elif analysis_type == "State Analysis":
    state = st.sidebar.selectbox("Select State", df["State"].unique())
    primary_param = st.sidebar.selectbox("Select Primary Parameter", ["Population", "Male", "Female", "Literate"])
    secondary_param = st.sidebar.selectbox("Select Secondary Parameter", ["Population", "Male", "Female", "Literate"])

    st.header(f"State Analysis: {state}")
    state_df = df[df["State"] == state]
    fig = px.scatter_map(state_df,
                            lat="Latitude",
                            lon="Longitude",
                            hover_name="District",
                            size=primary_param,
                            map_style ="dark",
                            size_max=15, 
                            zoom=4,
                            color=secondary_param)
    st.plotly_chart(fig)