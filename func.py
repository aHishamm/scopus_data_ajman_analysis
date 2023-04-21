
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
OPTIONS = ['citation_range','document_type_range','document_type_citation',
           'document_type_range_bar','document_type_citation_bar','publication_stage_range','au_ranking_range_bar','au_ranking_range'
           ]
#reference dataframe 
REFERENCE_DF = pd.read_csv("Scopus data.csv")
REFERENCE_DF = REFERENCE_DF.sort_values(by='Percentile',ascending=False) 
REFERENCE_DF = REFERENCE_DF.drop_duplicates(subset='Title',keep='first') 
REFERENCE_DF = REFERENCE_DF.reset_index(drop=True)
REFERENCE_DF['AU_ranking'] = pd.cut(REFERENCE_DF['Percentile'],bins=[0,50,75,90,100],labels=['AU-C','AU-B','AU-A','AU-A*'])
REFERENCE_DF['AU_ranking'].fillna('AU-C',inplace=True) 
REFERENCE_DF = REFERENCE_DF.drop(columns=['Scopus Source ID', 'Citation Count', 'Scholarly Output',
       'Percent Cited', 'CiteScore', 'SNIP', 'SJR',
       'Scopus ASJC Code (Sub-subject Area)', 'Scopus Sub-Subject Area',
       'Percentile', 'RANK', 'Rank Out Of', 'Publisher', 'Type', 'Open Access',
       'Quartile', 'Top 10% (CiteScore Percentile)', 'URL Scopus Source ID',
       'Print ISSN', 'E-ISSN'])
def process_scopus_df(filepath): 
    df = pd.read_csv(filepath) 
    #replaced citation values by zero 
    df['Cited by'].replace(np.nan,0,inplace=True)
    df['Cited by'] = df['Cited by'].astype("int64")
    df = pd.merge(df,REFERENCE_DF,left_on='Source title',right_on='Title')
    return df
def main_func(option,startyear,endyear,df): 
    if option == 'citation_range': 
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            if endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            grouping = query.groupby('Year').sum()
            grouping.drop(['Page count'],axis=1,inplace=True)
            grouping = grouping.reset_index()
            fig = px.line(grouping,x='Year',y='Cited by', title='# of Citations per Year', markers = True)
            fig.update_layout(
                xaxis = dict(
                    tickmode = 'linear',
                    dtick = 1
                )
            )
            return fig
    elif option == 'document_type_range':
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            elif endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            #pivoting 
            pivoted = query.pivot_table(index=['Document Type'],aggfunc='size')
            reset_pivoted = pivoted.reset_index()
            reset_pivoted.columns = reset_pivoted.columns.map(str)
            reset_pivoted = reset_pivoted.rename(columns={'Document Type':'Document Type','0':'count'})
            fig = px.pie(reset_pivoted,values='count',names='Document Type',title='Breakdown by Document type: '+str(startyear)+' - '+str(endyear)) 
            return fig 
    elif option == 'au_ranking_range':
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            elif endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            #pivoting 
            pivoted = query.pivot_table(index=['AU_ranking'],aggfunc='size')
            reset_pivoted = pivoted.reset_index()
            reset_pivoted.columns = reset_pivoted.columns.map(str)
            reset_pivoted = reset_pivoted.rename(columns={'AU_ranking':'AU_ranking','0':'count'})
            fig = px.pie(reset_pivoted,values='count',names='AU_ranking',title='Breakdown by AU Ranking: '+str(startyear)+' - '+str(endyear)) 
            return fig 
    elif option == 'document_type_citation': 
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            if endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            #pivoting 
            fig = px.pie(query,values='Cited by',names='Document Type',title='Citations by Document Type: '+str(startyear)+' - '+str(endyear)) 
            return fig 
    elif option == 'document_type_range_bar': 
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            if endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            #pivoting 
            pivoted = query.pivot_table(index=['Document Type'],aggfunc='size')
            reset_pivoted = pivoted.reset_index()
            reset_pivoted.columns = reset_pivoted.columns.map(str)
            reset_pivoted = reset_pivoted.rename(columns={'Document Type':'Document Type','0':'count'})
            reset_pivoted = reset_pivoted.sort_values('count',ascending=False) 
            fig = px.bar(reset_pivoted,y='count',x='Document Type',title='Breakdown by Document type: '+str(startyear)+' - '+str(endyear)) 
            return fig 
    elif option == 'au_ranking_range_bar': 
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            if endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            #pivoting 
            pivoted = query.pivot_table(index=['AU_ranking'],aggfunc='size')
            reset_pivoted = pivoted.reset_index()
            reset_pivoted.columns = reset_pivoted.columns.map(str)
            reset_pivoted = reset_pivoted.rename(columns={'AU_ranking':'AU_ranking','0':'count'})
            reset_pivoted = reset_pivoted.sort_values('count',ascending=False) 
            fig = px.bar(reset_pivoted,x='count',color='AU_ranking',y='AU_ranking',title='Breakdown by AU Ranking: '+str(startyear)+' - '+str(endyear)) 
            return fig 
    elif option == 'document_type_citation_bar': 
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            if endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            query = query.sort_values('Cited by',ascending=False) 
            fig = px.histogram(query,y='Cited by',x='Document Type',title='Citations by Document Type: '+str(startyear)+' - '+str(endyear)) 
            return fig 
    elif option == 'publication_stage_range': 
            new_df = df.copy() 
            min_year = new_df['Year'].min()
            max_year = new_df['Year'].max() 
            if startyear < min_year: 
                startyear = min_year
            if endyear > max_year: 
                endyear = max_year
            if startyear is not None and endyear is not None: 
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None: 
                query = new_df[(new_df.Year >= min_year) & (new_df.Year <= endyear)]
            elif startyear is None and endyear is not None:
                query = new_df[(new_df.Year >= startyear) & (new_df.Year <= max_year)]
            #pivoting 
            pivoted = query.pivot_table(index=['Publication Stage'],aggfunc='size')
            reset_pivoted = pivoted.reset_index()
            reset_pivoted.columns = reset_pivoted.columns.map(str)
            reset_pivoted = reset_pivoted.rename(columns={'Publication Stage':'Publication Stage','0':'count'})
            fig = px.pie(reset_pivoted,values='count',names='Publication Stage',title='Breakdown by Publication Stage: '+str(startyear)+' - '+str(endyear)) 
            return fig 