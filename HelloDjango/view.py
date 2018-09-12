from django.http import HttpResponse
from django.shortcuts import render
 
def home(request):
    # return HttpResponse("Hello Django ! ")
    # return render(request, 'index.html')
    return HttpResponse('Hello django')

def route1(request):
    return HttpResponse("Hello route1 ! ")

def newIndex(request):
	# context          = {}
    # context['hello'] = 'Hello World!'
    # return render(request, 'hello.html', context)
    return render(request, 'index.html')