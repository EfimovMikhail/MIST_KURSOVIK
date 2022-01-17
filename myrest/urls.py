from django.conf.urls import re_path, path, include

urlpatterns = [
    re_path(r'^', include('myrest.urls')),
    path('admin/', admin.site.urls),
]

