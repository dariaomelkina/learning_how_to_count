import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from colors import button_font, button_bg1, question, title, button_bg2
from flask import Flask, render_template, make_response, session


def create_button(title, color, reference, margin):
    return dcc.Link(html.Button(title, style={'width': 400, 'height': 250, 'color': button_font, 'font-size': '50px',
                                              'display': 'inline-block', "background": color, 'margin-left': margin}),
                    href=reference,
                    refresh=True)


def two_options(reference1, reference2):
    return html.Div([create_button("YES", button_bg1, reference1, 0),
                     create_button("NO", button_bg2, reference2, 10)],
                    style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                           'justify-content': 'center'})


question_style = {'color': question, 'font-size': '30px',
                  'margin-top': 120, 'width': '100%', 'display': 'flex',
                  'align-items': 'center', 'justify-content': 'center'}

extra_info = [dcc.Markdown("Bonus Project for Probability & Statistics Course",
                           style={'color': 'grey', 'margin-left': 20, 'font-size': '15px',
                                  'display': 'inline-block'}), dcc.Link(children='GitHub',
                                                                        href='https://github.com/dariaomelkina/learning_how_to_count',
                                                                        refresh=True,
                                                                        style={'color': 'grey',
                                                                               'margin-left': 1000,
                                                                               'font-size': '15px',
                                                                               'display': 'inline-block'})]

start_link = dcc.Link(children='START ONCE AGAIN', href='/start',
                      refresh=True,
                      style={'color': '#B6B6CA',
                             'margin-left': 93,
                             'font-size': '15px'})

# Create app
server = Flask(__name__)
# Actually different on server
server.secret_key = b'_5#y2L"F4Q8'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'url(assets/reset.css)']
app = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets, routes_pathname_prefix='/')
app.title = "LEARNING HOW TO COUNT"
app.layout = html.Div([dcc.Markdown("WELCOME TO THE \"LEARNING HOW TO COUNT\"!",
                                    style={'color': title, 'width': '100%', 'display': 'flex', 'align-items': 'center',
                                           'justify-content': 'center', 'font-size': '35px', 'margin-top': 40}),
                       html.Div(dcc.Markdown(
                           "That projects aims to help you with problems, which involve counting number of ways some objects can be chosen, or arranged, or distributed, etc. We prepared some questions, which will lead you to right formulas with explanation and typical examples. Without further ado...",
                           style={'color': "#B6B6CA", 'width': 850, 'text-align': 'center'}),
                           style={'width': "100%", 'display': 'flex', 'align-items': 'center',
                                  'justify-content': 'center', 'font-size': '20px', 'margin-top': 4}),
                       html.Div(dcc.Link(html.Button("LET'S GET STARTED!",
                                                     style={'height': 200, 'color': button_font, 'font-size': '40px',
                                                            "background": "#6E50A3", "margin-top": 10}),
                                         href="/start",
                                         refresh=True),
                                style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                                       'justify-content': 'center'}),
                       dcc.Markdown(
                           "INTERESTED IN THESE TYPES OF PROBLEMS?",
                           style={'color': 'grey', 'width': '100%', 'display': 'flex', 'align-items': 'center',
                                  'justify-content': 'center', 'font-size': '15px', 'margin-top': 20}),
                       dcc.Markdown(
                           "PROBABILITY & STATISTICS COURSE IS FOR YOU!",
                           style={'color': 'grey', 'width': '100%', 'display': 'flex', 'align-items': 'center',
                                  'justify-content': 'center', 'font-size': '15px'}),
                       html.Div(extra_info,
                                style={'margin-top': 190}),
                       ])

start = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                  routes_pathname_prefix='/start/')
start.title = "LEARNING HOW TO COUNT"
start.layout = html.Div([dcc.Markdown("DO YOU NEED TO WORK WITH MULTIPLE OPERATIONS?", style=question_style),
                         two_options("/basic", "/order"),
                         dcc.Markdown("CHOOSE WISELY, NEO...",
                                      style={'color': 'grey', 'width': '100%', 'display': 'flex',
                                             'align-items': 'center',
                                             'justify-content': 'center', 'font-size': '15px', 'margin-top': 20}),
                         html.Div(extra_info,
                                  style={'margin-top': 220}),
                         ])

order = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                  routes_pathname_prefix='/order/')
order.title = "LEARNING HOW TO COUNT"
order.layout = html.Div([dcc.Markdown("IS ORDER A PRIORITY?", style=question_style),
                         two_options("/repeat", "/group"),
                         dcc.Markdown("CHOOSE WISELY, NEO...",
                                      style={'color': 'grey', 'width': '100%', 'display': 'flex',
                                             'align-items': 'center',
                                             'justify-content': 'center', 'font-size': '15px', 'margin-top': 20}),
                         html.Div(extra_info,
                                  style={'margin-top': 220}),
                         ])

repeat = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                   routes_pathname_prefix='/repeat/')
repeat.title = "LEARNING HOW TO COUNT"
repeat.layout = html.Div([dcc.Markdown("CAN OBJECTS REPEAT?", style=question_style),
                          two_options("/allocations", "/permutations"),
                          dcc.Markdown("CHOOSE WISELY, NEO...",
                                       style={'color': 'grey', 'width': '100%', 'display': 'flex',
                                              'align-items': 'center',
                                              'justify-content': 'center', 'font-size': '15px', 'margin-top': 20}),
                          html.Div(extra_info,
                                   style={'margin-top': 220}),
                          ])

group = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                  routes_pathname_prefix='/group/')
group.title = "LEARNING HOW TO COUNT"
group.layout = html.Div([dcc.Markdown("DO YOU HAVE TO GROUP OBJECTS?", style=question_style),
                         two_options("/multinomial", "/combinations"),
                         dcc.Markdown("CHOOSE WISELY, NEO...",
                                      style={'color': 'grey', 'width': '100%', 'display': 'flex',
                                             'align-items': 'center',
                                             'justify-content': 'center', 'font-size': '15px', 'margin-top': 20}),
                         html.Div(extra_info,
                                  style={'margin-top': 220}),
                         ])

basic = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                  routes_pathname_prefix='/basic/')
basic.title = "LEARNING HOW TO COUNT"
basic.layout = html.Div([dcc.Markdown("test", style={'font-size': '0px'}),
                         html.Div(start_link,
                                  style={'margin-top': 20}),
                         html.Div(extra_info,
                                  style={'margin-top': 650}),
                         ], style={'background-image': 'url("assets/basicpoc8.png")'})

allocations = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                        routes_pathname_prefix='/allocations/')
allocations.title = "LEARNING HOW TO COUNT"
allocations.layout = html.Div([dcc.Markdown("test", style={'font-size': '0px'}),
                               html.Div(start_link,
                                        style={'margin-top': 20}),
                               html.Div(extra_info,
                                        style={'margin-top': 650}),
                               ], style={'background-image': 'url()'})

permutations = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                         routes_pathname_prefix='/permutations/')
permutations.title = "LEARNING HOW TO COUNT"
permutations.layout = html.Div([dcc.Markdown("test", style={'font-size': '0px'}),
                                html.Div(start_link,
                                         style={'margin-top': 20}),
                                html.Div(extra_info,
                                         style={'margin-top': 650}),
                                ], style={'background-image': 'url()'})

multinomial = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                        routes_pathname_prefix='/multinomial/')
multinomial.title = "LEARNING HOW TO COUNT"
multinomial.layout = html.Div([dcc.Markdown("test", style={'font-size': '0px'}),
                               html.Div(start_link,
                                        style={'margin-top': 20}),
                               html.Div(extra_info,
                                        style={'margin-top': 650}),
                               ], style={'background-image': 'url()'})

combinations = dash.Dash(name=__name__, server=server, external_stylesheets=external_stylesheets,
                         routes_pathname_prefix='/combinations/')
combinations.title = "LEARNING HOW TO COUNT"
combinations.layout = html.Div([dcc.Markdown("test", style={'font-size': '0px'}),
                                html.Div(start_link,
                                         style={'margin-top': 20}),
                                html.Div(extra_info,
                                         style={'margin-top': 650}),
                                ], style={'background-image': 'url()'})


@app.server.route('/')
def index():
    resp = make_response(app)
    return resp


# Run the program
if __name__ == '__main__':
    app.run_server(debug=True)
