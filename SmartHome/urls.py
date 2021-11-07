from django.contrib import admin
from django.urls import path
from devices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register),
    path('unregister', views.unregister),
    path('get_weather', views.get_weather),
    path('webhook', views.webhook),
    path('check_boiling_water_timer', views.check_boiling_water_timer),
]
