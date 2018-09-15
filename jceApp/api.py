from django.http import HttpResponse
from jceApp.models import Model
import logging

def createSubscriber(request):
	logger = logging.getLogger('mylogger')
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	logger.addHandler(ch)

	logger.info('foobar')
	logger.info(request)
	logger.info(request.POST)
	logger.info(request.POST['qxwx_login_id'])
	# logger.info(request.GET)
	# logger.info(request.GET['qxwx_login_id'])

	conn = Model(qxwx_login_id=request.POST['qxwx_login_id'])
	conn.save()
	return HttpResponse("createSubscriber")
