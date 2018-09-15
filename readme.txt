1.运行项目
python manage.py runserver 0.0.0.0:8000

端口可以任意指定，避免与其他服务冲突


2.静态文件配置
/temlates 目录下配置静态文件，在localhost:8000/static/路径下访问
例如：localhost:8000/static/index.html


//TODO
3.接口配置及调用（暂定）

url.py中增加配置
urlpatterns = [
    url(r'^getCoreData$', view.getCoreData),
]

view.py中增加接口函数
def getCoreData(request):
    return HttpResponse("coreData")


4.SVN路径

jce项目的SVN路径
.\HelloDjango\HelloDjango\service\svn\jce_proj
执行svn命令的py文件必须放在这个目录下面
.\HelloDjango\HelloDjango\service\svn


