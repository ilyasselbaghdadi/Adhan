import datetime as dt
import requests
from json import loads
from time import sleep
from winsound import PlaySound, Beep, SND_FILENAME
parameters:dict = {
                "latitude": "45.480929",
                "longitude": "-73.440443"}
def set_times() -> list:
    weird_time: dt.datetime = dt.datetime.now()
    current_time: str = dt.datetime.strftime(weird_time, "%d-%m-%y")
    prayer_data: requests.Response = requests.get(f"https://api.aladhan.com/v1/timings/{current_time}",parameters)
    if prayer_data.status_code != 200:
        Beep(1000,1000)
        exit('Uh oh, the request didnt work')
    prayer_dict: dict = loads(prayer_data.text)['data']['timings']
    del prayer_dict["Sunrise"]
    del prayer_dict["Sunset"]
    del prayer_dict["Imsak"]
    del prayer_dict["Firstthird"]
    del prayer_dict["Lastthird"]
    prayer_times: list[int] = [value for value in prayer_dict.values()]
    return [prayer_dict,prayer_times]

prayer_dict,prayer_times = set_times()
while True:
    time: str = dt.datetime.strftime(dt.datetime.now(),'%H:%M')
    if time == "00:00":
        prayer_dict, prayer_times = set_times()
    if time in prayer_times:
        PlaySound("Abdul-Basit.wav",SND_FILENAME) # type: ignore
    sleep(60)

