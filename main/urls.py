from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),

    #path('opercode/<int:pk>/delete/', views.kroy_operation_code_delete, name='kroy_operation_code_delete'),
]


