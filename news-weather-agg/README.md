# How to run

$kubectl apply -f django-deployment.yaml
$kubectl get deploy django-app
$kubectl apply -f django-svc.yaml

To get confirm succes and get port:
$kubectl get svc django

then to access service go to:
http://localhost:<port> 