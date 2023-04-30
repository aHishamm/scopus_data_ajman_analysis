import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px 
import streamlit as st 
import func as fc 

#setting up streamlit 
st.set_page_config(layout='wide') 
#streamlit components 
scopus_df = st.file_uploader("Choose a scopus export csv file")
#All plots on the same screen at the same time (8 plots) 3 containers, 3 x 3 x 2 
if scopus_df is not None: 
    processed_df = fc.process_scopus_df(scopus_df) 
    startyear = st.number_input("What is the starting year?",1990,2030)
    endyear = st.number_input("What is the ending year?",1990,2030) 
    #modified params and returns for main_func
    fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8 = fc.main_func(startyear,endyear,processed_df) 
    with st.container(): 
        col1, col2, col3 = st.columns(3) 
        with col1:
            st.plotly_chart(fig1,use_container_width=True)
        with col2: 
            st.plotly_chart(fig2,use_container_width=True)
        with col3: 
            st.plotly_chart(fig3,use_container_width=True)
    with st.container(): 
        col1, col2, col3 = st.columns(3)
        with col1: 
            st.plotly_chart(fig4,use_container_width=True)
        with col2: 
            st.plotly_chart(fig5,use_container_width=True) 
        with col3: 
            st.plotly_chart(fig6,use_container_width=True)
    with st.container(): 
        col1,col2 = st.columns(2) 
        with col1: 
            st.plotly_chart(fig7,use_container_width=True) 
        with col2:
            st.plotly_chart(fig8,use_container_width=True) 
    
        