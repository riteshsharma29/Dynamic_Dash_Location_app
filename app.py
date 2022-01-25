import dash
from dash import Input, Output, dcc, html,State
import requests
import os
from whitenoise import WhiteNoise

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

# settings required to host files on Heroku
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="static/")


# this function will delete old location html and js
def delete_old():
    directory = "static/"
    test = os.listdir(directory)
    for item in test:
        if item.endswith(".html"):
            os.remove(os.path.join(directory, item))
        if item.endswith(".js"):
            os.remove(os.path.join(directory, item))

# Layout
app.layout = html.Div([
    html.Div([
        html.H1('Dynamic Location Dashboard',style={"color":"blue","fontStyle":"italic","fontWeight":"bold"}),
        html.Div([
            html.P('Connect with me on: ',style={"color":"green","fontStyle":"italic","fontWeight":"bold"}),
            html.A(
                html.Img(src='/static/linkedin.png', className='img'),
                href='https://www.linkedin.com/in/ritesh-sharma5/',target='_blank'
            ),
            html.A(
                html.Img(src='/static/youtube.png', className='img',),
                href='https://www.youtube.com/channel/UCmH_jmNBR5O9o8UA8UHjwag',target='_blank'
            ),
            html.A(
                html.Img(src='/static/github.png', className='img',
                         id='github'),
                href='https://github.com/riteshsharma29',target='_blank'
            )
        ])
    ], id='header-div'),
    html.Br(),
    dcc.Input(id='username', value='', type='text',placeholder='Enter Location/Address and click Submit',style={"width": "20%", "height":"100%",'textAlign': 'center'}),
    html.Button(id='submit-button', type='submit', children='SUBMIT',style={"width": "15%", "height":"100%",'textAlign': 'center','backgroundColor':'aqua',"fontWeight":"bold"}),
    html.Br(),
    html.Hr(),
    html.Div(id='output_div'),

])

@app.callback(Output('output_div', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('username', 'value')],
              )
# function to generate location html & js
def update_output(clicks, input_value):
    if clicks is not None and len(input_value) > 0:
        delete_old()
        location = input_value
        URL = "https://geocode.search.hereapi.com/v1/geocode"
        api_key = 'YOUR-API-KEY'  # Acquire from developer.here.com
        PARAMS = {'apikey': api_key, 'q': location}
        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']
        # generate location js file
        # Read in the file
        with open('static/source.js.txt', 'r') as file:
            filedata = file.read()
        # Replace the target string
        filedata = filedata.replace('latval', str(latitude))
        filedata = filedata.replace('lngval', str(longitude))
        filedata = filedata.replace('rndlat', str(latitude).split(".")[0])
        filedata = filedata.replace('rndlng', str(longitude).split(".")[0])
        # Write the js file out again
        with open('static/' + location + '.js', 'w') as file:
            file.write(filedata)
        # generate location html file
        # Write the html file out again
        with open('static/demo.html.txt', 'r') as file:
            filedata_2 = file.read()
        # Replace the target string
        filedata_2 = filedata_2.replace('demo.js', location + ".js")
        # Write the file out again
        with open('static/' + location + '.html', 'w') as file:
            file.write(filedata_2)
        return html.Iframe(src="static/" + location + ".html",
                           style={
                               "height": "450px",
                               "width": "100%"
                           })


if __name__ == '__main__':
    app.run_server(debug=True)