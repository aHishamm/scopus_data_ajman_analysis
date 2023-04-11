import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px 
import streamlit as st 
import func as fc 

#setting up streamlit 
st.set_page_config(layout='wide') 
optionList = fc.OPTIONS

#streamlit components 
scopus_df = st.file_uploader("Choose a scopus export csv file")
option_selectbox = st.selectbox('Select a plot you want to visualize',optionList)
if scopus_df is not None: 
    processed_df = fc.process_scopus_df(scopus_df) 
    startyear = st.number_input("What is the starting year?",1990,2030)
    endyear = st.number_input("What is the ending year?",1990,2030) 
    #pass all the params to the main func 
    if st.button("Process"): 
        fig = fc.main_func(option_selectbox, startyear,endyear,processed_df) 
        st.plotly_chart(fig,use_container_width=True) 