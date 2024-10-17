from django.urls import path
from .views import async_counter

urlpatterns = [
    path('contador/', async_counter, name='async_counter'),
]
