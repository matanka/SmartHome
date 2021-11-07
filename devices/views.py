from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from devices.models import Device
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from .global_func import get_current_temperature
import os
import requests

def send_signal(device, signal):
	try:
		data = {
			'signal': signal,
			'name': device.name,
			'type': device.type
		}
		requests.post(device.webhook_url, data)
	except Exception as e:
		print(e)
	

def get_weather(request):
	temp = get_current_temperature()
	signal = "NORMAL"
	if temp >= 30:
		signal = "HOT"
	elif temp <= 15:
		signal = "COLD"

	data = signal

	if os.environ["last_signal"] != signal:
		os.environ["last_signal"] = signal

		devices = Device.objects.all()

		for device in devices:
			send_signal(device, signal)


	return JsonResponse(data, safe=False)

@csrf_exempt
@require_POST
def webhook(request):
	name = request.POST.get('name', '')
	device_type = request.POST.get('type', '')
	signal = request.POST.get('signal', '')
	device, create = Device.objects.get_or_create(name=name, type=device_type)
	device.adjust(signal)


@csrf_exempt
@require_POST
def register(request):
	name = request.POST.get('name', '')
	device_type = request.POST.get('type', '')
	webhook_url = request.POST.get('webhook_url', '')

	if name == "" or device_type == "" or webhook_url == "":
		return HttpResponseForbidden()

	try:
		device, create = Device.objects.get_or_create(name=name, type=device_type, webhook_url=webhook_url)

		data = {
			'status' : 1,
			'data' : 'SUCCESS',
		}

	except IntegrityError as e: 
		data = {
			'status' : 0,
			'data' : "CHOOSE_DIFFERENT_NAME",
		}
	except Exception as e:
		data = {
			'status' : 0,
			'data' : str(e),
		}
	

	return JsonResponse(data, safe=False)


@csrf_exempt
@require_POST
def unregister(request):
	name = request.POST.get('name', '')
	device_type = request.POST.get('type', '')

	if name == "" or device_type == "":
		return HttpResponseForbidden()

	try:
		device = Device.objects.get(name=name, type=device_type)
		device.delete()
		data = {
			'status' : 1,
			'data' : 'SUCCESS',
		}
	except ObjectDoesNotExist:
		data = {
			'status' : 1,
			'data' : 'OBJECT_ALREADY_UNREGISTER',
		}
	except Exception as e:
		data = {
			'status' : 0,
			'data' : 'COULD_NOT_UNREGISTER',
		}
		print(e)

	return JsonResponse(data, safe=False)



	

	



