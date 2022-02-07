import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



url1 = 'https://raw.githubusercontent.com/TobiasScherl/electricity-dashboard/main/electricity_df_day.csv'
url2 = 'https://raw.githubusercontent.com/TobiasScherl/electricity-dashboard/main/electricity_df_hour.csv'
url3 = 
url4 =

df_day = pd.read_csv(url1)
df_hour = pd.read_csv(url2)
df_app = pd.read_csv(url3)
df_type = pd.read_csv(url4)


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

fig1 = px.bar(df_day, x="dayofweek", y="Consumption [Wh]")
fig2 = px.bar(df_hour, x="hour", y="Consumption [Wh]")
fig3 = px.pie(df_app, values='Power [W]', names='Name', title='Gesamter Energieverbrauch pro Gerät')
fig4 = px.bar(df_type, x="Type", y="Power [W]")



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
    html.Div([
        html.H1(children='Gesamter Energieverbrauch pro Gerät'),

        html.Div(children='''
            Energieverbrauch nach Gerät geordnet
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),  
    ]),
    html.Div([
        html.H1(children='Gesamter Energieverbrauch pro Gerätegruppe'),

        html.Div(children='''
            Energieverbrauch nach Gerätegruppe geordnet
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),  
    ]),
])

