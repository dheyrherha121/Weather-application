from fastapi import APIRouter,HTTPException,Depends, status
import requests
from .. import database
from ..auth2 import get_curent_user
from sqlalchemy.orm import session



router = APIRouter(
    prefix= '/Current Weather',
    tags= ['Current weather']
)
api_key = "43155ad1b40cf402395c590aab20fac1"
@router.get('/')
def CurrentWeather(appid: str, city: str,unit: str, db: session = Depends(database.get_db), current_user:int = Depends(get_curent_user)):
    try:

       base_url =  "http://api.openweathermap.org/data/2.5/weather?"
       url = base_url + "appid=" + appid+ "&q=" + city +"&unit=" + unit
       request = requests.get(url).json()['main']
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='Your network/credentials is not strong/correct')
           

    return {f'The current weather condition of your area is {request}'}



    
    