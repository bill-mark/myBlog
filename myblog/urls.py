
from django.conf.urls import url,include
from django.contrib import admin
from app.views import add_app,get_my_apps

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include("blog.urls",namespace='blog')),
    url(r'^blog2/',include("blog2.urls")),
    url(r'^app/add_app',add_app),
    url(r'app/get_my_apps',get_my_apps),
]
