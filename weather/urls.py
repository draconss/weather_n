from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Start.as_view()),
    path('data_city/',data_city, name="data_city"),
    path('data/', Data_C.as_view(),name="data"),
]