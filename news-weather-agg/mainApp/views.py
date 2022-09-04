from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as bs
from .models import NewsField, City
from .forms import CityForm
from .keys import *

def wp_scraper(session):
    url = "https://www.washingtonpost.com/"
    content = session.get(url).content
    soup = bs(content, "html.parser")
    stories = soup.find_all("div", {"class": "left wrap-text art-size--lg"})
    for story in stories:
        image = story.find("img", src=True)
        if image == None:
            image = ""
        else:
            image = image["src"]
        link = story.find("a", {"data-pb-local-content-field": "web_headline"})
        title = link.find_next("span").text
        subtitle = story.find("div", {"class": "pb-xs font-size-blurb lh-fronts-tiny font-light gray-dark"})
        if subtitle == None:
            subtitle = " "
        else:
            subtitle = subtitle.find_next("span").text
        new_news = NewsField()
        new_news.title = title
        new_news.link = link["href"]
        new_news.image = image
        new_news.subtitle = subtitle
        new_news.source = url
        new_news.save()


def scraper(request):
    NewsField.objects.all().delete()
    session = requests.Session()
    session.headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" }
    # fetch articles from the Washington Post
    # load into datastructure
    wp_scraper(session)

    # fetch articles from the New York Times
    # load into datastructure

    # fetch articles from CNN
    # load into datastructure

    return redirect("../")


def weatherCall(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?APPID={}'.format(api_key)
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                response = requests.get(url + "&q={}".format(new_city)).json()
                if response['cod'] == 200:
                    form.save()
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        response = requests.get(url + "&q={}".format(city)).json()
        city_weather = {
            'city' : city.name.capitalize(),
            'temperature' : round(int(response['main']['temp']) - 273.15,2), # convert to celcius
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data, 
        'form' : form,
        }
    return context


def news_and_weather(request):
    news_ = NewsField.objects.all()[::-1]
    weather_ = weatherCall(request)
    return render(request, "mainApp/home.html", {'object_list': news_, 'weather': weather_})

# does not remove from db
def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')