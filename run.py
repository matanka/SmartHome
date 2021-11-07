import requests
import json

device_name_map = {'1': 'a/c', '2': 'switch', '3': 'water_heater'}

def register(name, device_type, webhook_url):
	data = {
		'name': name,
		'type': device_type,
		'webhook_url': webhook_url
	}
	response = requests.post("http://localhost:8000/register", data)
	if response.status_code != 200:
		raise Exception("SERVER_ERROR")
	json_data = json.loads(response.text)
	if str(json_data['status']) == '1':
		print('Device register successfully!')
	else:
		print('Device failed to register!')
		print(json_data['data'])
	return json_data

def unregister(name, device_type, webhook_url):
	data = {
		'name': name,
	}
	response = requests.post("http://localhost:8000/unregister", data)
	if response.status_code != 200:
		raise Exception("SERVER_ERROR")
	json_data = json.loads(response.text)
	if str(json_data['status']) == '1':
		print('Device unregister successfully!')
	else:
		print('Device failed to register!')
		print(json_data)
	return json_data

def main():
	print("Welcome to SmartHome device register!")
	print('_'*20)
	print("You can quit at any step by pressing Ctrl + z.")

	while True:
		print("Please select:\n1) To register\n2) To unregister")
		operation = str(input())
		if operation == '1' or operation == '2':
			break

	while True:
		print("Please select which device type do you want to register:")
		print("1) A/C\n2)Switch\n3)Water heater")
		device_type = str(input())
		if device_type == '1' or device_type == '2' or device_type == '3':
			break

	device_type = device_name_map[device_type]

	print("Please enter the name of the device:")
	name = str(input())

	print("Please enter the webhook url for the device:")
	webhook_url = str(input())

	if operation == '1':
		register(name, device_type, webhook_url)
	else:
		unregister(name, device_type, webhook_url)



if __name__ == '__main__':
	main()