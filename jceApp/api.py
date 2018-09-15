from django.http import HttpResponse
from jceApp.models import Model

def createSubscriber(request):
    conn = Model(qxwx_login_id='testb')
    conn.save()
    return HttpResponse("createSubscriber")
