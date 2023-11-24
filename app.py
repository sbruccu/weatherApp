from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = "d851b77b4d174ed3243c5a20189b7208"  

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        return redirect(url_for('weather', city=city))
    return render_template('index.html')

@app.route('/weather/<city>')
def weather(city):
    weather_data = get_weather_data(city)
    if weather_data:
        return render_template('weather.html', weather_data=weather_data, city=city)
    else:
        return "Weather information not available for this city."

if __name__ == '__main__':
    app.run(debug=True)
