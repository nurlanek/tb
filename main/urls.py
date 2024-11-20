from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path("", views.index, name="home"),
    path('index_detail/<int:id>/', views.index_detail, name='index_detail'),
]