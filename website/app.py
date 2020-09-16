import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from colors import button_font, button_bg1, question, title, button_bg2
from flask import Flask, render_template, make_response, session

# Create app
server = Flask(__name__)
# Actually different on server
server.secret_key = b'_5#y2L"F4Q8'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'url(assets/reset.css)']
app = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/')
app.title = "LEARNING HOW TO COUNT"
app.layout = html.Div([dcc.Markdown("WELCOME TO THE 'LEARNING HOW TO COUNT'!",
                                    style={'color': title, 'margin-left': 400, 'font-size': '30px', 'margin-top': 40}),
                       dcc.Markdown("INITIAL QUESTION?",
                                    style={'color': question, 'margin-left': 580, 'font-size': '30px',
                                           'margin-top': 20}),
                       html.Div([dcc.Link(html.Button("first choice 1",
                                                      style={'width': 400, 'height': 250, 'color': button_font,
                                                             'margin-left': 300, 'font-size': '30px',
                                                             'display': 'inline-block', "background": button_bg1}),
                                          href='/1',
                                          refresh=True),
                                 dcc.Link(html.Button("second choice 1",
                                                      style={'width': 400, 'height': 250, "background": button_bg2,
                                                             'color': button_font, 'margin-left': 10,
                                                             'font-size': '30px',
                                                             'display': 'inline-block'}), href='/2',
                                          refresh=True)]),
                       dcc.Markdown("CHOOSE WISELY, NEO...",
                                    style={'color': 'grey', 'margin-left': 620, 'font-size': '15px', 'margin-top': 20}),
                       html.Div([dcc.Markdown("Bonus Project for Probability&Statistics Course",
                                              style={'color': 'grey', 'margin-left': 20, 'font-size': '15px',
                                                     'display': 'inline-block'}), dcc.Link(children='GitHub',
                                                                                           href='https://github.com/dariaomelkina/learning_how_to_count',
                                                                                           refresh=True,
                                                                                           style={'color': 'grey',
                                                                                                  'margin-left': 1000,
                                                                                                  'font-size': '15px',
                                                                                                  'display': 'inline-block'})],
                                style={'margin-top': 220}),
                       ])

app1 = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/1/')
app1.title = "LEARNING HOW TO COUNT"
# style={'color': title_color,
#                             'font-size': '25px', 'display': 'inline-block', 'margin-left': 100, 'margin-top': 5}),
app1.layout = html.Div([dcc.Markdown("ANOTHER QUESTION? (1)",
                                     style={'color': question, 'margin-left': 520, 'font-size': '30px',
                                            'margin-top': 50}),
                        html.Div([dcc.Link(html.Button("first choice 2",
                                                       style={'width': 400, 'height': 250, 'color': button_font,
                                                              'margin-left': 300, 'font-size': '30px',
                                                              'display': 'inline-block', "background": button_bg1}),
                                           href='/fin',
                                           refresh=True),
                                  dcc.Link(html.Button("second choice 2",
                                                       style={'width': 400, 'height': 250, "background": button_bg2,
                                                              'color': button_font, 'margin-left': 10,
                                                              'font-size': '30px',
                                                              'display': 'inline-block'}), href='/fin',
                                           refresh=True)]),
                        dcc.Markdown("CHOOSE WISELY, NEO...",
                                     style={'color': 'grey', 'margin-left': 620, 'font-size': '15px',
                                            'margin-top': 20}),
                        html.Div([dcc.Markdown("Bonus Project for Probability&Statistics Course",
                                               style={'color': 'grey', 'margin-left': 20, 'font-size': '15px',
                                                      'display': 'inline-block'}), dcc.Link(children='GitHub',
                                                                                            href='https://github.com/dariaomelkina/learning_how_to_count',
                                                                                            refresh=True,
                                                                                            style={'color': 'grey',
                                                                                                   'margin-left': 1000,
                                                                                                   'font-size': '15px',
                                                                                                   'display': 'inline-block'})],
                                 style={'margin-top': 220}),
                        ])

app2 = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/2/')
app2.title = "LEARNING HOW TO COUNT"

app2.layout = html.Div([dcc.Markdown("ANOTHER QUESTION? (2)",
                                     style={'color': question, 'margin-left': 520, 'font-size': '30px',
                                            'margin-top': 50}), html.Div([dcc.Link(html.Button("first choice 2",
                                                                                               style={'width': 400,
                                                                                                      'height': 250,
                                                                                                      'color': button_font,
                                                                                                      'margin-left': 300,
                                                                                                      'font-size': '30px',
                                                                                                      'display': 'inline-block',
                                                                                                      "background": button_bg1}),
                                                                                   href='/fin',
                                                                                   refresh=True),
                                                                          dcc.Link(html.Button("second choice 2",
                                                                                               style={'width': 400,
                                                                                                      'height': 250,
                                                                                                      "background": button_bg2,
                                                                                                      'color': button_font,
                                                                                                      'margin-left': 10,
                                                                                                      'font-size': '30px',
                                                                                                      'display': 'inline-block'}),
                                                                                   href='/fin',
                                                                                   refresh=True)]),
                        dcc.Markdown("CHOOSE WISELY, NEO...",
                                     style={'color': 'grey', 'margin-left': 620, 'font-size': '15px',
                                            'margin-top': 20}),
                        html.Div([dcc.Markdown("Bonus Project for Probability&Statistics Course",
                                               style={'color': 'grey', 'margin-left': 20, 'font-size': '15px',
                                                      'display': 'inline-block'}), dcc.Link(children='GitHub',
                                                                                            href='https://github.com/dariaomelkina/learning_how_to_count',
                                                                                            refresh=True,
                                                                                            style={'color': 'grey',
                                                                                                   'margin-left': 1000,
                                                                                                   'font-size': '15px',
                                                                                                   'display': 'inline-block'})],
                                 style={'margin-top': 220}),
                        ])

fin = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/fin/')
fin.title = "LEARNING HOW TO COUNT"
fin.layout = html.Div([dcc.Markdown("Final page!", style={'color': question, 'font-size': '45px'}),
                       html.Div([dcc.Markdown("Bonus Project for Probability&Statistics Course",
                                              style={'color': 'grey', 'margin-left': 20, 'font-size': '15px',
                                                     'display': 'inline-block'}), dcc.Link(children='GitHub',
                                                                                           href='https://github.com/dariaomelkina/learning_how_to_count',
                                                                                           refresh=True,
                                                                                           style={'color': 'grey',
                                                                                                  'margin-left': 1000,
                                                                                                  'font-size': '15px',
                                                                                                  'display': 'inline-block'})],
                                style={'margin-top': 220}),
                       ])


@app.server.route('/')
def index():
    resp = make_response(app)
    return resp


# Run the program
if __name__ == '__main__':
    app.run_server(debug=True)
