import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.getenv("Weather_API")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form["city"]
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params={"q": city, "appid": WEATHER_API , "units" : "metric"})
    data = response.json()
    if data["cod"] != 200:
     return render_template("index.html", error="City not found!")

    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    country_code = data["sys"].get("country", "africa is not  a city")
    return render_template("index.html", city=city, temp=temp, humidity=humidity, description=description, wind_speed=wind_speed, country_code=country_code)
    

if __name__ == "__main__":
    app.run(debug=True)