from django.conf.urls import url
from myrest import views

urlpatterns = [
    url(r'^api/myrest$', views.merop_list),
    url(r'^api/myrest/(?P<pk>[0-9]+)$', views.merop_detail),
    url(r'^api/myrest/published$', views.merop_list_published)
]
