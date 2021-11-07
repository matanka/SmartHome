from django.db import models
from .global_func import calculate_time_to_arrive
from datetime import datetime

TYPE_CHOICES = (
	('a/c', 'Air Conditioner'),
	('switch', 'Switch'),
	('water_heater', 'Water Heater'),
)

def ac_logic(state, signal):
	if signal == 'HOT':
		state["switch"] = True
		state["temp"] = state["temp"] - 10
		print("Decrease temperature by 10 degrees")
	elif signal == "COLD":
		state["switch"] = True
		state["temp"] = state["temp"] + 13
		print("Increase temperature by 13 degrees")
	else:
		state["switch"] = False
		print("Turn off a/c")

	return state
		
def switch_logic(state, signal):
	if signal == 'HOT':
		state["light"] = False
		print("Turn light off")
	elif signal == "COLD":
		state["light"] = True
		print("Turn light on")

	return state

def water_heater_logic(state, signal):
	if signal == "COLD":
		if calculate_time_to_arrive():
			state["switch"] = True
			state["switch_on_time"] = str(datetime.now())
			print("Turn on water heater for 25 minutes")

	return state

adjust_logic = {
	'a/c': ac_logic,
	'switch': switch_logic,
	'water_heater': water_heater_logic
}

class Device(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
	type =  models.CharField(max_length=50, choices=TYPE_CHOICES, blank=False, null=False)
	webhook_url = models.URLField(max_length=255, blank=True, null=True)
	state = models.JSONField("ContactInfo", default={}, blank=False, null=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.state == {} or self.state is None or self.state == "":
			if self.type == "a/c":
				self.state = {"temp": 25, "switch": False, "last_signal": "Normal"}
			elif self.type == "switch":
				self.state = {"light": False, "last_signal": "Normal"}
			elif self.type == "water_heater":
				self.state = {"switch": False, "last_signal": "Normal", "switch_on_time": str(datetime.now())}

		super(Device, self).save(*args, **kwargs)


	def to_json(self):
		return {
			'name': self.name,
			'type': self.type,
			'webhook_url': self.webhook_url
		}

	def adjust(self, signal):
		if self.state["last_signal"] != signal:
			state = adjust_logic[self.type](self.state, signal)
			self.state["last_signal"] = signal
			self.state = state
			self.save()



