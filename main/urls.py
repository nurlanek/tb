from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path("", views.index, name="home"),
    #path("index", views.index),
    path('index_detail/<int:project_id>/', views.index_detail, name='index_detail'),
]



