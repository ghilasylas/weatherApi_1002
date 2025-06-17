from datetime import datetime
from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import uvicorn

load_dotenv()
app = FastAPI()

CITY = "London"
API_KEY = "20ba69e7192d543f70ce7b23aea01e0a"


def get_weather():
    url=f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        weather= {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:

        weather = {
            'city':'unknown',
            'temperature': 'n/a',
            'description': 'enable to go data'
        }
    return weather


@app.get("/info")
async def get_info():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")

    weather= get_weather()

    return {
        "date": formatted_date,
        "time": formatted_time,
        "weather": weather
    }