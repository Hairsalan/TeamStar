import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/news')
def news():
    weather_data = get_weather("Williamston,Michigan")  
    return render_template('news.html', weather_data=weather_data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/permits_and_forms')
def permits_and_forms():
    return render_template('permits_and_forms.html')

@app.route('/city_calendar')
def city_calendar():
    return render_template('city_calendar.html')

def get_weather(city):
    api_key = "f6e4fee65fd681cfca40c3c5f6127f16"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'  # You can use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)

        print("API Request URL:", response.url)
        print("API Response Status Code:", response.status_code)
        print("API Response Text:", response.text)

        data = response.json()

        weather_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }

        return weather_info

    except requests.RequestException as e:
        print("Error making API request:", e)
        return None
    except Exception as e:
        print("Unexpected error:", e)
        return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)