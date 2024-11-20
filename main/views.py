from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from regproje.models import (
    Dolboor, Project_confirmation, Negizgimaalymat, Kenenmaalymat,
    Iskeashyruuplany, Dolboordundudjeti, Dolboordunkomandasy,
    Baaloo_turuktuuluk, Tirkemeler
)

def index(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    dolboorlor = Dolboor.objects.all()

    context = {
        'dolboorlor' : dolboorlor,
    }

    return render(request, "main/index.html", context)

@login_required
def index_detail(request, id):
    dolboor = get_object_or_404(Dolboor, id=id)
    user = dolboor.user

    user_projects = Dolboor.objects.filter(user=user)
    negizgimaalymat = Negizgimaalymat.objects.filter(user=user)
    kenenmaalymat = Kenenmaalymat.objects.filter(user=user)
    iskeashyruuplany = Iskeashyruuplany.objects.filter(user=user)
    dolboordundudjeti = Dolboordundudjeti.objects.filter(user=user)
    dolboordunkomandasy = Dolboordunkomandasy.objects.filter(user=user)
    baaloo_turuktuuluk = Baaloo_turuktuuluk.objects.filter(user=user).first()
    tirkemeler = Tirkemeler.objects.filter(user=user)

    context = {
        'dolboor': dolboor,
        'user_projects': user_projects,
        'negizgimaalymat': negizgimaalymat,
        'kenenmaalymat': kenenmaalymat,
        'iskeashyruuplany': iskeashyruuplany,
        'dolboordundudjeti': dolboordundudjeti,
        'dolboordunkomandasy': dolboordunkomandasy,
        'baaloo_turuktuuluk': baaloo_turuktuuluk,
        'tirkemeler': tirkemeler,
    }


    return render(request, "main/index_detail.html", context)