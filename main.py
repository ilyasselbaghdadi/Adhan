import datetime
import json
import requests
from playsound3 import playsound # type: ignore
from pyttsx3 import speak # type: ignore
from time import sleep
parameters = {
                "latitude": "45.480929",
                "longitude": "-73.440443"}
def set_times() -> list:
    weird_time = datetime.datetime.now()
    current_time = datetime.datetime.strftime(weird_time, "%d-%m-%y")
    prayer_data = requests.get(f"https://api.aladhan.com/v1/timings/{current_time}",parameters)
    if prayer_data.status_code != 200:
        exit('Uh oh, the request didnt work')
    prayer_dict: dict = json.loads(prayer_data.text)['data']['timings']
    prayer_times: list[int] = [value for value in prayer_dict.values()]
    return [prayer_dict,prayer_times]

prayer_dict,prayer_times = set_times()
while True:
    time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
    if time == "00:00":
        prayer_dict, prayer_times = set_times()
    if time in prayer_times:
        speak(f"It is time for {prayer_dict.get(time)}")
        playsound("Abdul-Basit.mp3")
    sleep(60)

