from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "953c4353becfb95d9493ad2b7b129295"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url)

            if res.status_code == 200:
                data = res.json()
                weather_data = {
                    "city": data["name"],
                    "temp": round(data["main"]["temp"]),
                    "desc": data["weather"][0]["description"].capitalize(),
                    "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"]
                }
            else:
                error = " City not found. Please try again!"
        else:
            error = "⚠️ Please enter a city name!"

    return render_template("home.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
