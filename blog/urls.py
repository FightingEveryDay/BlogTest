from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'', views.index, name = 'index'), # 这里什么都没有的匹配要放最后,不然匹配不到下面的资源
]