# Dynamic_Dash_Location_app
Dynamic Dash Location app deployed on Heroku



# For running app in local install dependencies using command : pip install -r requirements.txt
# Acquire your Javascript api key from developer.here.com. Am using Freemium A/C. replace YOUR-API-KEY string with your api key in app.py and static/source.js.txt and save the file.

# For deployment follow this link https://dash.plotly.com/deployment. Below are the steps I followed on Ubuntu Virtual box:

cd /home/<user>/Desktop/Dynamic-Location-app <br>
git init <br>
heroku create dynamic-location-app # change my-dash-app to a unique name <br>
git add . # add all files to git <br>
git commit -m 'message' <br>
git push heroku master # deploy code to heroku <br>


For redeployment follow below steps :<br>

git status # view the changes <br>
git add .  # add all the changes <br>
git commit -m 'a description of the changes' <br>
git push heroku master <br>
