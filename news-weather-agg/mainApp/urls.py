from django.urls import path
from mainApp.views import scraper, news_and_weather, delete_city

urlpatterns = [
  path('scraper/', scraper, name="scrape"),
  path('', news_and_weather, name="home"),
  path('delete/<city_name>/', delete_city, name='delete_city'),
]