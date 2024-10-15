from django.urls import path
from . import views
from .views import menin_dolboorum

app_name = 'regproje'

urlpatterns = [
    path("index", views.index, name="index"),
    #path("menin_dolboorum", views.Menin_dolboorum, name="menin_dolboorum"),
    path('menin_dolboorum/', menin_dolboorum, name='menin_dolboorum'),

    path('approvers/menim-dolboorum/<int:dolboor_id>/', views.approvers_menin_dolboorum,
         name='approvers_menin_dolboorum'),
    path('confirm/', views.project_confirmation_view, name='project_confirmation'),

    path("Dolboordundudjeti", views.Dolboordundudjeti, name="Dolboordundudjeti"),
    path("Dolboordunkomandasy", views.Dolboordunkomandasy, name="Dolboordunkomandasy"),
    path("Baaloo_turuktuuluk", views.Baaloo_turuktuuluk, name="Baaloo_turuktuuluk"),
    path("Tirkemeler", views.Tirkemeler, name="Tirkemeler"),

    path('dolboor_list/', views.dolboor_list, name='dolboor_list'),
    path('create/', views.dolboor_create, name='dolboor_create'),
    path('edit/<int:pk>/', views.dolboor_edit, name='dolboor_edit'),
    path('delete/<int:pk>/', views.dolboor_delete, name='dolboor_delete'),

    path('negizgimaalymat_list/', views.negizgimaalymat_list, name='negizgimaalymat_list'),
    path('negizgimaalymat/create/', views.negizgimaalymat_create, name='negizgimaalymat_create'),
    path('negizgimaalymat/<int:pk>/edit/', views.negizgimaalymat_edit, name='negizgimaalymat_edit'),
    path('negizgimaalymat/<int:pk>/delete/', views.negizgimaalymat_delete, name='negizgimaalymat_delete'),

    path('kenenmaalymat/', views.kenenmaalymat_list, name='kenenmaalymat_list'),
    path('kenenmaalymat/create/', views.kenenmaalymat_create, name='kenenmaalymat_create'),
    path('kenenmaalymat/<int:pk>/edit/', views.kenenmaalymat_edit, name='kenenmaalymat_edit'),
    path('kenenmaalymat/<int:pk>/delete/', views.kenenmaalymat_delete, name='kenenmaalymat_delete'),

    path('iskeashyruuplany/', views.iskeashyruuplany_list, name='iskeashyruuplany_list'),
    path('iskeashyruuplany/create/', views.iskeashyruuplany_create, name='iskeashyruuplany_create'),
    path('iskeashyruuplany/<int:pk>/edit/', views.iskeashyruuplany_edit, name='iskeashyruuplany_edit'),
    path('iskeashyruuplany/<int:pk>/delete/', views.iskeashyruuplany_delete, name='iskeashyruuplany_delete'),

    path('dolboordundudjeti/', views.dolboordundudjeti_list, name='dolboordundudjeti_list'),
    path('dolboordundudjeti/create/', views.dolboordundudjeti_create, name='dolboordundudjeti_create'),
    path('dolboordundudjeti/edit/<int:pk>/', views.dolboordundudjeti_edit, name='dolboordundudjeti_edit'),
    path('dolboordundudjeti/delete/<int:pk>/', views.dolboordundudjeti_delete, name='dolboordundudjeti_delete'),

    path('dolboordunkomandasy/', views.dolboordunkomandasy_list, name='dolboordunkomandasy_list'),
    path('dolboordunkomandasy/create/', views.dolboordunkomandasy_create, name='dolboordunkomandasy_create'),
    path('dolboordunkomandasy/edit/<int:pk>/', views.dolboordunkomandasy_edit, name='dolboordunkomandasy_edit'),
    path('dolboordunkomandasy/delete/<int:pk>/', views.dolboordunkomandasy_delete, name='dolboordunkomandasy_delete'),

    path('baaloo_turuktuuluk/', views.baaloo_turuktuuluk_list, name='baaloo_turuktuuluk_list'),
    path('baaloo_turuktuuluk/create/', views.baaloo_turuktuuluk_create, name='baaloo_turuktuuluk_create'),
    path('baaloo_turuktuuluk/edit/<int:pk>/', views.baaloo_turuktuuluk_edit, name='baaloo_turuktuuluk_edit'),
    path('baaloo_turuktuuluk/delete/<int:pk>/', views.baaloo_turuktuuluk_delete, name='baaloo_turuktuuluk_delete'),

    path('tirkemeler/', views.tirkemeler_list, name='tirkemeler_list'),
    path('tirkemeler/create/', views.tirkemeler_create, name='tirkemeler_create'),
    path('tirkemeler/edit/<int:pk>/', views.tirkemeler_edit, name='tirkemeler_edit'),
    path('tirkemeler/delete/<int:pk>/', views.tirkemeler_delete, name='tirkemeler_delete'),
]
