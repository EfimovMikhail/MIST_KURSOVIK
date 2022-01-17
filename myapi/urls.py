from django.contrib import admin
from django.urls import path, include
from .views import merop_list, merop_detail, merop_list_published



urlpatterns = [
    path('merop_list', merop_list),
    path('details/<int:pk>', merop_detail),
    path('published', merop_list_published),

]