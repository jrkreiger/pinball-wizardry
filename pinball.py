import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_csv('pinball_data.csv')
makers = data.manufacturer.unique()

app.layout = html.Div(children=[
    html.H1(children='Pinball Wizardry'),

    html.Div(children='''
        Explore the makers of pinball machines.
    '''),

    html.Div(children='Choose your player:'),

    html.Div([
        dcc.Dropdown(
            id='makers',
            options=[{'label':i, 'value':i} for i in makers],
            value='All'
        )],
    style={'width': '15%', 'display': 'inline-block'}
    ),

    dcc.Graph(
        id='units-graph',
        figure={
            'data': [
                {'y': [name for name in data.name],
                 'x': [unit for unit in data.units],
                 'type': 'bar'},
            ],
            'layout': {
                'title': 'Machines produced'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

