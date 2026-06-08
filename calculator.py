from datetime import datetime,timedelta
from math import acos,cos,tan,pi,sin
def dtr(angle):
    return (angle/360)*2*pi
def declination():
    day = int(datetime.now().strftime("%j"))
    dec_angle = dtr(23.45*sin(2*pi/365*(day-81)))
    return dec_angle
def fajr_calculator(latitude,longitude):
    now = datetime.now()
    latitude = dtr(latitude)
    longitude = dtr(longitude)
    cosofha = -tan(latitude)*tan(declination()) -sin(dtr(18))/(cos(latitude)*cos(declination()))
    hour_angle = acos(cosofha)/(2*pi)*360/15
    print(hour_angle)
    time = datetime(now.year,now.month,now.day,12,0)-timedelta(hours=hour_angle)
    return time
if __name__ == "__main__":
    print(fajr_calculator(45.480929,-73.440443))