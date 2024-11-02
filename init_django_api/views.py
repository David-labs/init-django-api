from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Init_django_api")