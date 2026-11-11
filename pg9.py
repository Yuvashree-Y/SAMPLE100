from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "c66b2270da6e46e687772206260710"

@app.route('/weather')
def weather():
    city = request.args.get('city', 'Bangalore')

    url = "https://api.weatherapi.com/v1/current.json"

    response = requests.get(
        url,
        params={"key": API_KEY, "q": city}
    )

    if response.status_code != 200:
        return jsonify({"error": "Invalid city or API key"}), 400

    data = response.json()

    return jsonify({
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"],
        "wind_speed": data["current"]["wind_kph"]
    })


if __name__ == "__main__":
    app.run(debug=True)