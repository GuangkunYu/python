from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('demo/', demo),
    path('bootstrap/', bootstrap),
    path('get_avg_api/', get_avg_api),
    path('get_opt_api/', get_opt_api),
]