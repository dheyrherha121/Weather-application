from  fastapi import FastAPI
from .routers import currentWeather,login,users
app = FastAPI()

app.include_router(currentWeather.router)
app.include_router(login.router)
app.include_router(users.router)

@app.get('/')
def index():
    return {'welcome, this is a fastapi application that will healp read weather forcast of your area.'}
