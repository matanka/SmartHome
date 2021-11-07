# SmartHome

This project use both device and controller with the same code base.
For easy use you can use the same server to mimic both of them on the same server.

This project use sqlite as DB by default.
you can use the current DB or run the migrations by yourself.
the user/password for the admin are:
root/123qweasd

Install
________

create your virtualenv with Python 3.7.0 and then install the requirements:
pip install -r requirements.txt

Activate the virtualenv and then run the server by using:
python manage.py runserver

This project include the file run.py which used to register and unrigster the devices.
Use another terminal while the server is running in order to use it.

The settings of when the person arrives home is located inside settings.py by the name TIME_TO_GET_HOME.

Make sure to runserver before running the registartions.

In order to fetch the data from the data provider you need to run cronjob in your server to run every hour (0 * * * *).
For easy use to fetch the data, I've created the url /get_weather to mimic this functionality.
