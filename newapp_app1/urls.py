from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from testapp import views   # デフォルトからの追記部分

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),   # デフォルトからの追記部分
    path('testapp/', include('testapp.urls')),    # デフォルトからの追記部分
]
