from django.conf.urls import re_path
from myrest import views

urlpatterns = [
    re_path(r'^api/myrest$', views.merop_list),
    re_path(r'^api/myrest/(?P<pk>[0-9]+)$', views.merop_detail),
    re_path(r'^api/myrest/published$', views.merop_list_published)
]
