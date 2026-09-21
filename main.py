from fastapi import FastAPI
from fastapi import APIRouter
from weather_service import CurrentWeather

router = APIRouter(prefix="/weather",tags=["Weather"])


app=FastAPI()
app.include_router(router)

@router.get("/{latitude}/{longitude}")
def get_weather(latitude: float, longitude: float):

    return CurrentWeather(latitude, longitude)

