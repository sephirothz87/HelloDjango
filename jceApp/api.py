from django.http import HttpResponse
from jceApp.models import Model
import json
import logging

def createSubscriber(request):
	logger = logging.getLogger("django")

	logger.info('start')

	qxwx_login_id = request.POST['qxwx_login_id']

	res = {'code':9999,'msg':'未知错误'}

	try:
		rdp = Model.objects.get(qxwx_login_id=qxwx_login_id)
	except Model.DoesNotExist:
		conn = Model(qxwx_login_id=qxwx_login_id)
		conn.save()
		logger.info('订阅成功')
		res={'code':0,'msg':'订阅成功'}
		return HttpResponse(json.dumps(res), content_type="application/json")
		
	logger.info(rdp)
	logger.info('已订阅')
	res = {'code':1,'msg':'该用户已经订阅'}
	return HttpResponse(json.dumps(res), content_type="application/json")