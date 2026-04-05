import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="India Census Dashboard", page_icon=":bar_chart:", layout="wide")

#------------------------------------------------------------

df = pd.read_csv("dataset/india.csv")
l = list(df['State'].unique())
l.insert(0,"Overall Analysis")
df['Literacy rate'] = round((df['Literate']/df['Population'])*100,2)
param = sorted(df.columns)
param.insert(0,"None")
total_pop = df["Population"].sum()
total_lit = df["Literate"].sum()
avg_litracy_rate = round((total_lit/total_pop)*100,2)
sex_ratio = round((df['Female'].sum()/df['Male'].sum())*1000)

col1, col2 ,col3, col4= st.columns(4)
col1.metric("Total Population", f"{(total_pop)/10000000:.2f} Cr")
col2.metric("Total Literate", f"{(total_lit)/10000000:.2f} Cr")
col3.metric("Average Literacy Rate", f"{avg_litracy_rate}%")
col4.metric("Sex ratio ",sex_ratio)

#----------------------------------------------------------


st.sidebar.title("India Census Dashboard")
analysis_type = st.sidebar.selectbox("Select Analysis Type", ['None',"Overall Analysis", "State Analysis"])
# btn1 = st.sidebar.button("submit")

if analysis_type == "Overall Analysis":
    primary_param = st.sidebar.selectbox("Select Primary Parameter", param)
    secondary_param = st.sidebar.selectbox("Select Secondary Parameter", param)
    if primary_param == 'None' or secondary_param == 'None':
        st.warning("Please select both primary and secondary parameters.")
    else:
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
    primary_param = st.sidebar.selectbox("Select Primary Parameter", param)
    secondary_param = st.sidebar.selectbox("Select Secondary Parameter", param)
    st.header(f"State: {state} Analysis")

    state_df = df[df["State"] == state]
    if primary_param == 'None' or secondary_param == 'None':
        st.warning("Please select both primary and secondary parameters.")
    else:
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
