import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np, random, operator

# from travel_salesman import geneticAlgorithm
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

df_data = pd.read_csv("lugares.csv", index_col=0)


px.set_mapbox_access_token(open("keys/mapbox_token").read())
fig = px.scatter_mapbox(df_data,
                        lat='LATITUDE',
                        lon='LONGITUDE',
                        hover_name='NOME',
                        zoom=1)

map = dbc.Row([
                dcc.Graph(id="map-graph", figure=fig)
            ], style={"height": "80vh"})

# ================================
# Tempalte
app.layout = dbc.Container(
        children=[
                dbc.Row([
                        dbc.Col([
                                map
                                ], md=9),
                ])
        ], fluid=True, )

# ========================================================

if __name__ == '__main__':
    # app.run_server(debug=True)
	server = app.server
	app.scripts.config.serve_locally = True
	server = app.server
	app.run_server(host="0.0.0.0", port="8050")