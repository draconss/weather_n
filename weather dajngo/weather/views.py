from django.http import JsonResponse
from django.shortcuts import render,redirect
import requests
from test_1.settings import API_KEY_W
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import City,Weath
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.

import json
def data_city(req):
    if req.is_ajax():
        data = req.GET['term']
        if len(data) >= 3:
            data_c = City.objects.filter(name__icontains=data)
            ex = []
            for i in data_c:
                ex.append({"id":i.pk,"text":i.name})
            return JsonResponse({"results": ex})
        else:
            return JsonResponse({})

class Start(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'start.html')

    def post(self, request, *args, **kwargs):
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=imperial&appid={}'
        city_weather = requests.get(url.format(city,API_KEY_W)).json()
        if(city_weather.get('cod') and city_weather.get('cod') == 200):
            data = Weath()
            data.city = City.objects.get(pk=city)
            data.temp = city_weather.get('main').get('temp')
            data.humidity = city_weather.get('main').get('humidity')
            data.pressure = city_weather.get('main').get('pressure')
            data.temp_max = city_weather.get('main').get('temp_max')
            data.temp_min = city_weather.get('main').get('temp_min')
            data.wind_deg = city_weather.get('wind').get('speed')
            data.wind_speed = city_weather.get('wind').get('deg')
            data.save()
            return redirect('data/?code={}'.format(data.id))

        return render(request, 'start.html',{'err':'city not found'})



class Data_C(ListView):
    model = City
    template_name = 'data.html'
    paginate_by = 5
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super(Data_C, self).get_context_data(**kwargs)
        quer = 'select weather_city.id, name from weather_city ' \
               'inner join weather_Weath ' \
               'on weather_city.id = weather_Weath.city_id ' \
               'group by name'
        context['city'] = City.objects.raw(quer)
        return context

    def get_queryset(self):
        data = Weath.objects.all()
        if (self.request.GET.get('city')):
            data = data.filter(city__name=self.request.GET.get('city'))
        if (self.request.GET.get('date_form')):
            data = data.filter(date__gte=self.request.GET.get('date_form'))
        if (self.request.GET.get('date_to')):
            data = data.filter(date__lte=self.request.GET.get('date_to'))
        return data


