# How to run

Create file news-weather-agg/mainApp/keys.py containing: api_key = "<your_openweathermap_api_key>"

$kubectl apply -f django-deployment.yaml 

$kubectl get deploy django-app

$kubectl apply -f django-svc.yaml


To get confirm successful deployment and get port:
$kubectl get svc django

then to access service go to:
http://localhost:port 
