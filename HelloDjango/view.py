from django.http import HttpResponse
 
def home(request):
    return HttpResponse("Hello Django ! ")

def route1(request):
    return HttpResponse("Hello route1 ! ")