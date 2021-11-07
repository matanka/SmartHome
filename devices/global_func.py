from datetime import datetime
from django.conf import settings
import requests
import json
import geocoder


def get_current_time():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	return current_time

FMT = '%H:%M:%S'
def calculate_time_to_arrive():
	t1 = get_current_time()
	t2 = settings.TIME_TO_GET_HOME
	tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
	if tdelta.seconds <= 3600:
		return True
	else:
		return False

def get_current_temperature():
	g = geocoder.ip('me')
	lat = g.latlng[0]
	lon = g.latlng[1]

	data = {
		'units': 'metric',
		'lat': lat,
		'lon': lon,
		'appid': settings.OPEN_WEATHER_KEY
	}
	response = requests.get("http://api.openweathermap.org/data/2.5/weather", data)
	if response.status_code != 200:
		raise Exception("SERVER_ERROR")
	json_data = json.loads(response.text)
	current_temp = int(json_data['main']['temp'])
	print(current_temp)
	return current_temp
