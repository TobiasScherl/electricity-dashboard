#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install dash')


# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# In[3]:


df = pd.read_csv(r'C:\Users\tobis\Downloads\electricity_df_day.csv')
df_hour = pd.read_csv(r'C:\Users\tobis\Downloads\electricity_df_hour.csv')


# In[9]:


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

fig1 = px.bar(df, x="dayofweek", y="Consumption [Wh]")
fig2 = px.bar(df_hour, x="hour", y="Consumption [Wh]")


app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Täglicher Stromverbrauch'),

        html.Div(children='''
            Energieverbrauch nach Wochentagen geordnet
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Stündlicher Energieverbrauch'),

        html.Div(children='''
            Energieverbrauch nach Stunden geordnet
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
])


# In[10]:


if __name__ == '__main__':
    app.run_server()


# In[ ]:





# In[ ]:




