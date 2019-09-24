import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='Try out a multiply'
initial_value='1,2,3'
longtext='''
        _Suggestions you might try:_
        * 1,3,6,7
        * 4,8,12
        * 6,9,10
        '''
tabtitle = ''
sourceurl = ''
githublink = 'https://github.com/caroleonor/dash-simple-callback/edit/master/app.py'

########### Define a function for your callback:
def multiply(list_number):
    total =1
    for x in list_number:
        total*=x
    return total


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div(children=[dcc.Markdown(longtext)]),
    dcc.Input(id='my-id', value=initial_value, type='text'),
    html.Div(id='my-div'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    a=multiply(input_value)
    return f"You've entered '{input_value}', and your output is '{a}'"

############ Deploy
if __name__ == '__main__':
    app.run_server()
