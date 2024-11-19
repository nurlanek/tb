from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
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

#@login_required
def index_detail(request, project_id):
    if not request.user.is_authenticated:
        return redirect("account:login")

    try:
        # Projeyi ID'ye göre al
        dolboor = get_object_or_404(Dolboor, id=project_id, is_active=True)
    except Http404:
        return redirect("error_page")  # Hata sayfasına yönlendirme

    # Kullanıcıya bağlı verileri çek
    user_projects = Dolboor.objects.filter(user=request.user)
    negizgimaalymat = Negizgimaalymat.objects.filter(dolboor=dolboor)
    kenenmaalymat = Kenenmaalymat.objects.filter(dolboor=dolboor)
    iskeashyruuplany = Iskeashyruuplany.objects.filter(dolboor=dolboor)
    dolboordundudjeti = Dolboordundudjeti.objects.filter(dolboor=dolboor)
    dolboordunkomandasy = Dolboordunkomandasy.objects.filter(dolboor=dolboor)
    baaloo_turuktuuluk = Baaloo_turuktuuluk.objects.filter(dolboor=dolboor).first()
    tirkemeler = Tirkemeler.objects.filter(dolboor=dolboor)

    # Şablon bağlamı
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