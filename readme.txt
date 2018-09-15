1.运行项目
python manage.py runserver 0.0.0.0:8000

端口可以任意指定，避免与其他服务冲突


2.静态文件配置
/temlates 目录下配置静态文件，在localhost:8000/static/路径下访问
例如：localhost:8000/static/index.html


//TODO
3.接口配置及调用

-在根目录新建App
django-admin startapp jceApp

-建立api.py文件，处理请求用
from django.http import HttpResponse

def createSubscriber(request):
    return HttpResponse("createSubscriber")

-在urls.py中增加如下配置
from . import api
urlpatterns = [
    url(r'^createSubscriber$', api.createSubscriber),
]

-在根目录的urls.py中include该app
url(r'^jceApp/', include("jceApp.urls")),

-在页面ajax用如下url请求
url: "../jceApp/createSubscriber",


4.SVN路径

jce项目的SVN路径
.\HelloDjango\HelloDjango\service\svn\jce_proj
执行svn命令的py文件必须放在这个目录下面
.\HelloDjango\HelloDjango\service\svn


5.DB配置

-首先复用app的路径配置

-在app的根目录，修改models.py，定义字段名和表名
-如果不自定义表名，会以app名+model作为表名，例如jceApp_model
class Model(models.Model):
	# id = models.AutoField()
	qxwx_login_id = models.CharField(max_length=20)

	class Meta:
		db_table='jce_change_subscriber'

