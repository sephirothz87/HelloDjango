from django.http import HttpResponse
from jceApp.models import Model
import logging

def createSubscriber(request):
	logger = logging.getLogger('mylogger')
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	logger.addHandler(ch)

	# logger.info('foobar')
	# logger.info(request)
	# logger.info(request.POST)
	# logger.info(request.POST['qxwx_login_id'])
	# logger.info(request.GET)
	# logger.info(request.GET['qxwx_login_id'])

	qxwx_login_id = request.POST['qxwx_login_id']

	try:
		rdp = Model.objects.get(qxwx_login_id=qxwx_login_id)
	except Model.DoesNotExist:
		conn = Model(qxwx_login_id=qxwx_login_id)
		conn.save()
		return HttpResponse("createSubscriber")
		

	# if rdp == None:
	# 	conn = Model(qxwx_login_id=qxwx_login_id)
	# 	conn.save()
	# 	return HttpResponse("createSubscriber")
	# else:
	logger.info(rdp)
	return HttpResponse("already exist")
	# TODO  根据不同情况返回错误码和信息