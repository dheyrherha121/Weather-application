from  fastapi import FastAPI
from .routers import currentWeather
app = FastAPI()

app.include_router(currentWeather.router)

@app.get('/')
def index():
    return {'welcome, this is a fastapi application that will healp read weather forcast of your area.'}
