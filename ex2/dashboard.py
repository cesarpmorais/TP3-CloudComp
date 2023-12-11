from dash import Dash, html, dash_table, dcc
from dash.dependencies import Input, Output

import json
import pandas as pd
from collections import deque
import redis

from mocker import Mocker

app = Dash(__name__)

def get_redis_data():
    redis_client = redis.Redis(host="192.168.121.66", port=6379, db=0)
    decoded_data = redis_client.get("cesarmorais-proj3-output").decode('utf-8')
    return json.loads(decoded_data)

redis_dict = get_redis_data()

# Add table
df = pd.DataFrame(list(redis_dict.items()), columns=['Metric', 'Value'])
df = df[:2]

# Add cpu data watch
cpu_data = {f'avg-cpu{i}-60sec': deque(maxlen=20) for i in range(16)}

app.layout = html.Div([
    html.H1(
        children="Monitoring Dashboard",
        style={'fontWeight': 'bold', 'text-align': 'center'}
    ),
    
    dash_table.DataTable(
        id='table',
        columns=[
            {'name': 'Metric', 'id': 'Metric'},
            {'name': 'Value', 'id': 'Value'}
        ],
        data=df.to_dict('records'),
        style_header={'fontWeight': 'bold', 'text-align': 'center'},
        style_cell={'text-align': 'center'}
    ),
    
    dcc.Graph(id='cpu-graph'),
    html.Button('Update Data', id='update-button', n_clicks=0),
    dcc.Interval(
        id='interval-component',
        interval=1 * 60 * 1000,  # in milliseconds, update every 1 minute
        n_intervals=0
    ),
])

# Callback to update data for both table and graph
@app.callback(
    [Output('cpu-graph', 'figure'),
     Output('table', 'data')],
    [Input('update-button', 'n_clicks'),
     Input('interval-component', 'n_intervals')]
)
def update_data(n_clicks, n_intervals):
    redis_dict = get_redis_data()

    # Retrieve CPU data from Redis
    cpu_values = {f'avg-cpu{i}-60sec': float(redis_dict.get(f'avg-cpu{i}-60sec', 0)) for i in range(16)}

    # Update deque with new values
    for cpu, value in cpu_values.items():
        cpu_data[cpu].append(value)

    # Create plotly figure
    figure = {
        'data': [
            {'x': list(range(1, 20 + 1)), 'y': list(cpu_data[cpu]), 'name': cpu}
            for cpu in cpu_data
        ],
        'layout': {
            'title': 'Moving Average CPU Usage',
            'xaxis': {'title': 'Time'},
            'yaxis': {'title': 'CPU Usage (%)'},
        }
    }

    # Update table data
    df = pd.DataFrame(list(redis_dict.items()), columns=['Metric', 'Value'])
    df = df[:2]
    table_data = df.to_dict('records')

    return figure, table_data


if __name__ == '__main__':
    app.run(debug=True)