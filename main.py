import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

app = dash.Dash()
app.title = "Stock Visualization"
app.layout = html.Div(children=[
    html.H1('Stock Visualization Dashboard'),
    html.H4('Nairobi Securities Exchange'),
    dcc.Input(id="input", value='', type='text'),
    html.Div(id="output-graph")
])


