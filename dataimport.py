import psycopg2
import requests
from config import DB_CONFIG, API_KEY
from datetime import datetime

# Connect to database
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# Create insert function
def insert_data(city, district, state, temp, humidity, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO weather_data (city, district, state, temperature, humidity, weather_description, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (city, district, state, temp, humidity, description, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

# Fetch weather from OpenWeather
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    cities = [
        {"city": "Mumbai", "district": "Mumbai", "state": "Maharashtra"},
        {"city": "Pune", "district": "Pune", "state": "Maharashtra"},
        {"city": "Nagpur", "district": "Nagpur", "state": "Maharashtra"},
        {"city": "Nashik", "district": "Nashik", "state": "Maharashtra"},
        {"city": "Thane", "district": "Thane", "state": "Maharashtra"},
        {"city": "Aurangabad", "district": "Aurangabad", "state": "Maharashtra"}
    ]

    for c in cities:
        weather = fetch_weather(c["city"])
        temp = weather["main"]["temp"]
        humidity = weather["main"]["humidity"]
        description = weather["weather"][0]["description"]
        insert_data(c["city"], c["district"], c["state"], temp, humidity, description)

    print("Weather data inserted successfully ✅")
