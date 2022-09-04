FROM ubuntu:20.04

RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip

RUN pip install django gunicorn psycopg2-binary

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/

ADD news-weather-agg /app

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "news-weather-agg.wsgi"]