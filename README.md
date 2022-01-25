# Dynamic_Dash_Location_app
Dynamic Dash Location app deployed on Heroku

https://dash.plotly.com/deployment

## For running app in local install dependencies using command : pip install -r requirements.txt
## Acquire your Javascript api key from developer.here.com. Am using Freemium A/C. replace YOUR-API-KEY string with your api key in app.py and static/source.js.txt and save the file.

## For deployment follow below steps on Ubuntu:

cd /home/<user>/Desktop/Dynamic-Location-app
git init
heroku create dynamic-location-app # change my-dash-app to a unique name
git add . # add all files to git
git commit -m 'message'
git push heroku master # deploy code to heroku


For redeployment follow below steps :

git status # view the changes
git add .  # add all the changes
git commit -m 'a description of the changes'
git push heroku master
