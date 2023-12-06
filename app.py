import requests
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS #CORS gives permission for website to access when running server on local (for testing)
from db import get_db

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


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

#endpoint to edit cms community page text in the database
@app.route('/edit_community_page_text', methods=['POST'])
def edit_community_page_text():
    db = get_db()
    cursor = db.cursor()

    number = request.json.get('number')
    content = request.json.get('content')

    if number is not None and content is not None:
        # Update statement
        update_query = "UPDATE cmsCommunityPage SET content = %s WHERE number = %s"

        # Execute the update query
        cursor.execute(update_query, (content, number))
        db.commit()

        cursor.close()
        return jsonify({"message": "Data updated successfully"})
    else:
        cursor.close()
        return jsonify({"error": "Invalid request data"})

#endpoint to get cms community page text from database
@app.route('/get_community_page_text', methods=['GET'])
def get_community_page_text():
    db = get_db()  # Use the function from database.py to connect to the database
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM cmsCommunityPage")
        data = cursor.fetchall()
        return jsonify({'data': data})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        #db.close()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
