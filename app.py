from matplotlib import markers
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="India Census Dashboard", page_icon=":bar_chart:", layout="wide")

#------------------------------------------------------------
#data cleaning

states = pd.read_csv("dataset/state_population.csv")
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


#----------------------------------------------------------

#main code


st.title("India Census Dashboard")
tab1, tab2 = st.tabs(["Overview", "Detailed Analysis"])

with tab1:

    col1, col2 ,col3, col4= st.columns(4)

    col1.metric("Total Population", f"{(total_pop)/10000000:.2f} Cr")
    col2.metric("Total Literate", f"{(total_lit)/10000000:.2f} Cr")
    col3.metric("Literacy Rate", f"{avg_litracy_rate}%")
    col4.metric("Sex ratio ",sex_ratio)

    # tab10, tab20 , tab30 = st.tabs(["Population", "Literacy Rate",'sex ratio'])

    with st.expander("Scatter Map of Population Distribution Across States"): 

        fig = px.scatter_map(states,
                            lat="Latitude",
                            lon="Longitude",
                            hover_name="State", 
                            map_style ="dark",
                            size = "Population",
                            color = "Population",
                            size_max=15, 
                            title="Population Distribution Across State",
                            zoom=2.5,
                            color_discrete_sequence=["#00FFFF"])
        st.plotly_chart(fig)


    with st.expander("Population vs Literacy Rate"):
            fig3 = px.line(states,
                            x='State',
                            y=['Population', 'Literate'],
                            hover_name="State",
                            markers=True,  
                            title='Population vs Literacy Rate Across States'
                            )

            st.plotly_chart(fig3, use_container_width=True)

            states['literacy_rate'] = round((states['Literate']/states['Population'])*100,2)
            s = states[states['literacy_rate'] == states['literacy_rate'].max()]['State']
            #st.write(f"The state with the highest literacy rate is {s.values[0]} with a literacy rate of {states['literacy_rate'].max()}%")
            st.info(f"The state with the highest literacy rate is {s.values[0]} with a literacy rate of {states['literacy_rate'].max()}%")
    #st.caption(f"The state with the highest literacy rate is {s.values[0]} with a literacy rate of {states['literacy_rate'].max()}%")
#     st.markdown("""
# ### 📊 Fact
# - Kerala has the highest literacy rate in India  
# - Bihar has one of the lowest literacy rates  
# """)


    with st.expander("Bar chart of top populated states"):
            try :
                num = st.text_input("Enter number of top states to display",
                                    value="5"
                                    )
                top = states[["State", "Population"]].sort_values(by="Population", ascending=False).head(int(num))

            except ValueError:
                st.error("Please enter a valid number.")
                top = states[["State", "Population"]].sort_values(by="Population", ascending=False).head()

            fig2 = px.bar(top ,
                        x="State",
                        y="Population",
                        color="Population",
                        title=f"Top {num} Populated States in India"
                        )
            st.plotly_chart(fig2)


