import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import Flask, render_template, make_response, session

# Create app
server = Flask(__name__)
# Actually different on server
server.secret_key = b'_5#y2L"F4Q8'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/')
app.title = "LEARN HOW TO COUNT"
app.layout = html.Div([html.Div([dcc.Link(html.Button("first choice 1", style={'color':'violet'}), href='/1',
                       refresh=True),
                        dcc.Link(html.Button("second choice 1", style={'color':'green'}), href='/2',
                                 refresh=True)])
                        ])

app1 = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/1/')
app1.title = "LEARN HOW TO COUNT"

app1.layout = html.Div([dcc.Markdown("Final page!"),
                        dcc.Link(html.Button("first choice 2", style={'color':'violet'}), href='/fin',
                       refresh=True),
                        dcc.Link(html.Button("second choice 2", style={'color':'green'}), href='/fin',
                                 refresh=True)
                        ])

app2 = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/2/')
app2.title = "LEARN HOW TO COUNT"

app2.layout = html.Div([dcc.Link(html.Button("first choice 2", style={'color':'violet'}), href='/fin',
                       refresh=True),
                        dcc.Link(html.Button("second choice 2", style={'color':'green'}), href='/fin',
                                 refresh=True)
                        ])

fin = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/fin/')
fin.title = "LEARN HOW TO COUNT"
fin.layout = html.Div([dcc.Markdown("Final page!")
                        ])

@app.server.route('/')
def index():
    resp = make_response(app)
    return resp

# Run the program
if __name__ == '__main__':
    app.run_server(debug=True)
