from django.shortcuts import render, redirect, get_object_or_404
from .models import (Dolboor, Negizgimaalymat, Kenenmaalymat, Iskeashyruuplany, Project_confirmation,
                     Dolboordundudjeti, Dolboordunkomandasy, Baaloo_turuktuuluk,Tirkemeler)
from .forms import (DolboorForm, NegizgimaalymatForm, KenenmaalymatForm, TirkemelerForm,
                    IskeAshyruUplanyForm, DolboordundudjetiForm, DolboordunkomandasyForm,
                    ProjectConfirmationForm, BaalooTuruktuulukForm)
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    # Kullanıcının tüm Dolboor kayıtlarını al
    dolboors = Dolboor.objects.all()

    dolboor_data = []
    for dolboor in dolboors:
        # Kullanıcının bu dolboor için olan son onayını al
        last_confirmation = Project_confirmation.objects.filter(dolboor=dolboor, user=request.user).order_by('-created').first()
        dolboor_data.append({
            'dolboor': dolboor,
            'last_confirmation': last_confirmation,
        })

    # Template'e verileri gönder
    return render(request, "regproje/index.html", {'dolboor_data': dolboor_data})

@login_required
def approvers_menin_dolboorum(request, dolboor_id):
    dolboor = get_object_or_404(Dolboor, id=dolboor_id)
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

    return render(request, "regproje/register/approvers_menin_dolboorum.html", context)



def Menin_dolboorum(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    return render(request, "regproje/register/menin_dolboorum.html")

def dolboor_list(request):
    dolboor_list = Dolboor.objects.filter(user=request.user)
    if not dolboor_list:
        return redirect('regproje:dolboor_create')
    return render(request, "regproje/register/reg-2.html", {'dolboor_list': dolboor_list})

def dolboor_create(request):
    if request.method == 'POST':
        form = DolboorForm(request.POST)
        if form.is_valid():
            dolboor = form.save(commit=False)
            dolboor.user = request.user
            dolboor.save()
            return redirect('regproje:dolboor_list')
    else:
        form = DolboorForm()
    return render(request, "regproje/register/reg-2.html", {'form': form})

def dolboor_edit(request, pk):
    dolboor = get_object_or_404(Dolboor, pk=pk)
    if request.method == 'POST':
        form = DolboorForm(request.POST, instance=dolboor)
        if form.is_valid():
            form.save()
            return redirect('regproje:dolboor_list')
    else:
        form = DolboorForm(instance=dolboor)
    return render(request, "regproje/register/reg-2.html", {'form': form, 'dolboor': dolboor})

def dolboor_delete(request, pk):
    dolboor = get_object_or_404(Dolboor, pk=pk)
    if request.method == 'POST':
        dolboor.delete()
        return redirect('regproje:dolboor_list')
    return render(request, "regproje/register/dolboor_confirm_delete.html", {'dolboor': dolboor})

# negizgimaalimat basi
def negizgimaalymat_list(request):

    negizgimaalymat_list = Negizgimaalymat.objects.filter(user=request.user)

    if not negizgimaalymat_list:  # Eğer queryset boşsa
        return redirect('regproje:negizgimaalymat_create')
    return render(request, 'regproje/register/reg-1.html', {'negizgimaalymat_list': negizgimaalymat_list})

def negizgimaalymat_create(request):
    if request.method == 'POST':
        form = NegizgimaalymatForm(request.POST)
        if form.is_valid():
            negizgimaalymat = form.save(commit=False)
            negizgimaalymat.user = request.user
            negizgimaalymat.save()
            return redirect('regproje:negizgimaalymat_list')
    else:
        form = NegizgimaalymatForm()
    return render(request, 'regproje/register/reg-1.html', {'form': form})


def negizgimaalymat_edit(request, pk):
    negizgimaalymat = get_object_or_404(Negizgimaalymat, pk=pk)
    if request.method == 'POST':
        form = NegizgimaalymatForm(request.POST, instance=negizgimaalymat)
        if form.is_valid():
            form.save()
            return redirect('regproje:negizgimaalymat_list')
    else:
        form = NegizgimaalymatForm(instance=negizgimaalymat)
    return render(request, 'regproje/register/reg-1.html', {'form': form})

def negizgimaalymat_delete(request, pk):
    negizgimaalymat = get_object_or_404(Negizgimaalymat, pk=pk)
    if request.method == 'POST':
        negizgimaalymat.delete()
        return redirect('regproje:negizgimaalymat_list')
    return render(request, 'regproje/register/negizgimaalymat_confirm_delete.html', {'negizgimaalymat': negizgimaalymat})
# negizgimaalimat buttu

def kenenmaalymat_list(request):
    kenenmaalymat_list = Kenenmaalymat.objects.filter(user=request.user)
    if not kenenmaalymat_list:
        return redirect('regproje:kenenmaalymat_create')
    return render(request, "regproje/register/kenenmaalymat.html", {'kenenmaalymat_list': kenenmaalymat_list})

def kenenmaalymat_create(request):
    if request.method == 'POST':
        form = KenenmaalymatForm(request.POST)
        if form.is_valid():
            kenenmaalymat = form.save(commit=False)
            kenenmaalymat.user = request.user
            kenenmaalymat.save()
            return redirect('regproje:kenenmaalymat_list')
    else:
        form = KenenmaalymatForm()
    return render(request, "regproje/register/kenenmaalymat.html", {'form': form})

def kenenmaalymat_edit(request, pk):
    kenenmaalymat = get_object_or_404(Kenenmaalymat, pk=pk)
    if request.method == 'POST':
        form = KenenmaalymatForm(request.POST, instance=kenenmaalymat)
        if form.is_valid():
            form.save()
            return redirect('regproje:kenenmaalymat_list')
    else:
        form = KenenmaalymatForm(instance=kenenmaalymat)
    return render(request, "regproje/register/kenenmaalymat.html", {'form': form, 'kenenmaalymat': kenenmaalymat})

def kenenmaalymat_delete(request, pk):
    kenenmaalymat = get_object_or_404(Kenenmaalymat, pk=pk)
    if request.method == 'POST':
        kenenmaalymat.delete()
        return redirect('regproje:kenenmaalymat_list')
    return render(request, "regproje/register/kenenmaalymat_confirm_delete.html", {'kenenmaalymat': kenenmaalymat})

def iskeashyruuplany_list(request):
    iskeashyruuplany_list = Iskeashyruuplany.objects.filter(user=request.user)
    if not iskeashyruuplany_list:
        return redirect('regproje:iskeashyruuplany_create')
    return render(request, "regproje/register/reg-3.html", {'iskeashyruuplany_list': iskeashyruuplany_list})

def iskeashyruuplany_create(request):
    if request.method == 'POST':
        form = IskeAshyruUplanyForm(request.POST)
        if form.is_valid():
            iskeashyruuplany = form.save(commit=False)
            iskeashyruuplany.user = request.user
            iskeashyruuplany.save()
            return redirect('regproje:iskeashyruuplany_list')
    else:
        form = IskeAshyruUplanyForm()
    return render(request, "regproje/register/reg-3.html", {'form': form})

def iskeashyruuplany_edit(request, pk):
    iskeashyruuplany = get_object_or_404(Iskeashyruuplany, pk=pk)
    if request.method == 'POST':
        form = IskeAshyruUplanyForm(request.POST, instance=iskeashyruuplany)
        if form.is_valid():
            form.save()
            return redirect('regproje:iskeashyruuplany_list')
    else:
        form = IskeAshyruUplanyForm(instance=iskeashyruuplany)
    return render(request, "regproje/register/reg-3.html", {'form': form, 'iskeashyruuplany': iskeashyruuplany})

def iskeashyruuplany_delete(request, pk):
    iskeashyruuplany = get_object_or_404(Iskeashyruuplany, pk=pk)
    if request.method == 'POST':
        iskeashyruuplany.delete()
        return redirect('regproje:iskeashyruuplany_list')
    return render(request, "regproje/register/iskeashyruuplany_confirm_delete.html", {'iskeashyruuplany': iskeashyruuplany})

def dolboordundudjeti_list(request):
    dolboordundudjeti_list = Dolboordundudjeti.objects.filter(user=request.user)
    if not dolboordundudjeti_list:
        return redirect('regproje:dolboordundudjeti_create')
    return render(request, "regproje/register/reg-4.html", {'dolboordundudjeti_list': dolboordundudjeti_list})

def dolboordundudjeti_create(request):
    if request.method == 'POST':
        form = DolboordundudjetiForm(request.POST)
        if form.is_valid():
            dolboordundudjeti = form.save(commit=False)
            dolboordundudjeti.user = request.user
            dolboordundudjeti.save()
            return redirect('regproje:dolboordundudjeti_list')
    else:
        form = DolboordundudjetiForm()
    return render(request, "regproje/register/reg-4.html", {'form': form})

def dolboordundudjeti_edit(request, pk):
    dolboordundudjeti = get_object_or_404(Dolboordundudjeti, pk=pk)
    if request.method == 'POST':
        form = DolboordundudjetiForm(request.POST, instance=dolboordundudjeti)
        if form.is_valid():
            form.save()
            return redirect('regproje:dolboordundudjeti_list')
    else:
        form = DolboordundudjetiForm(instance=dolboordundudjeti)
    return render(request, "regproje/register/reg-4.html", {'form': form})

def dolboordundudjeti_delete(request, pk):
    dolboordundudjeti = get_object_or_404(Dolboordundudjeti, pk=pk)
    if request.method == 'POST':
        dolboordundudjeti.delete()
        return redirect('regproje:dolboordundudjeti_list')
    return render(request, "regproje/register/dolboordundudjeti_confirm_delete.html", {'dolboordundudjeti': dolboordundudjeti})


def dolboordunkomandasy_list(request):
    dolboordunkomandasy_list = Dolboordunkomandasy.objects.filter(user=request.user)
    if not dolboordunkomandasy_list:
        return redirect('regproje:dolboordunkomandasy_create')
    return render(request, 'regproje/register/reg-5.html', {'dolboordunkomandasy_list': dolboordunkomandasy_list})

def dolboordunkomandasy_create(request):
    if request.method == 'POST':
        form = DolboordunkomandasyForm(request.POST)
        if form.is_valid():
            dolboordunkomandasy = form.save(commit=False)
            dolboordunkomandasy.user = request.user
            dolboordunkomandasy.save()
            return redirect('regproje:dolboordunkomandasy_list')
    else:
        form = DolboordunkomandasyForm()
    return render(request, 'regproje/register/reg-5.html', {'form': form})

def dolboordunkomandasy_edit(request, pk):
    dolboordunkomandasy = get_object_or_404(Dolboordunkomandasy, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DolboordunkomandasyForm(request.POST, instance=dolboordunkomandasy)
        if form.is_valid():
            form.save()
            return redirect('regproje:dolboordunkomandasy_list')
    else:
        form = DolboordunkomandasyForm(instance=dolboordunkomandasy)
    return render(request, 'regproje/register/reg-5.html', {'form': form})

def dolboordunkomandasy_delete(request, pk):
    dolboordunkomandasy = get_object_or_404(Dolboordunkomandasy, pk=pk, user=request.user)
    if request.method == 'POST':
        dolboordunkomandasy.delete()
        return redirect('regproje:dolboordunkomandasy_list')
    return render(request, 'regproje/register/dolboordunkomandasy_confirm_delete.html', {'dolboordunkomandasy': dolboordunkomandasy})


def baaloo_turuktuuluk_list(request):
    baaloo_turuktuuluk_list = Baaloo_turuktuuluk.objects.filter(user=request.user)
    if not baaloo_turuktuuluk_list:
        return redirect('regproje:baaloo_turuktuuluk_create')
    return render(request, "regproje/register/reg-6.html", {'baaloo_turuktuuluk_list': baaloo_turuktuuluk_list})

def baaloo_turuktuuluk_create(request):
    if request.method == 'POST':
        form = BaalooTuruktuulukForm(request.POST)
        if form.is_valid():
            baaloo_turuktuuluk = form.save(commit=False)
            baaloo_turuktuuluk.user = request.user
            baaloo_turuktuuluk.save()
            return redirect('regproje:baaloo_turuktuuluk_list')
    else:
        form = BaalooTuruktuulukForm()
    return render(request, 'regproje/register/reg-6.html', {'form': form})

def baaloo_turuktuuluk_edit(request, pk):
    baaloo_turuktuuluk = get_object_or_404(Baaloo_turuktuuluk, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BaalooTuruktuulukForm(request.POST, instance=baaloo_turuktuuluk)
        if form.is_valid():
            form.save()
            return redirect('regproje:baaloo_turuktuuluk_list')
    else:
        form = BaalooTuruktuulukForm(instance=baaloo_turuktuuluk)
    return render(request, 'regproje/register/reg-6.html', {'form': form})

def baaloo_turuktuuluk_delete(request, pk):
    baaloo_turuktuuluk = get_object_or_404(Baaloo_turuktuuluk, pk=pk, user=request.user)
    if request.method == 'POST':
        baaloo_turuktuuluk.delete()
        return redirect('regproje:baaloo_turuktuuluk_list')
    return render(request, 'regproje/register/baaloo_turuktuuluk_confirm_delete.html', {'baaloo_turuktuuluk': baaloo_turuktuuluk})

def tirkemeler_list(request):
    tirkemeler_list = Tirkemeler.objects.filter(user=request.user)
    if not baaloo_turuktuuluk_list:
        return redirect('regproje:tirkemeler_create')
    return render(request, 'regproje/register/reg-7.html', {'tirkemeler_list': tirkemeler_list})

# 2. Tirkemeler Düzenleme
def tirkemeler_edit(request, pk):
    tirkeme = get_object_or_404(Tirkemeler, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TirkemelerForm(request.POST, request.FILES, instance=tirkeme)
        if form.is_valid():
            form.save()
            return redirect('regproje:tirkemeler_list')
    else:
        form = TirkemelerForm(instance=tirkeme)
    return render(request, 'regproje/register/reg-7.html', {'form': form})

# 3. Tirkemeler Silme

def tirkemeler_create(request):
    if request.method == 'POST':
        form = TirkemelerForm(request.POST, request.FILES)
        if form.is_valid():
            tirkeme = form.save(commit=False)
            tirkeme.user = request.user  # Giriş yapan kullanıcıyı ekler
            tirkeme.save()
            return redirect('regproje:tirkemeler_list')  # Başarılı ekleme sonrası yönlendirme
    else:
        form = TirkemelerForm()
    return render(request, 'regproje/register/reg-7.html', {'form': form})

def tirkemeler_delete(request, pk):
    tirkeme = get_object_or_404(Tirkemeler, pk=pk, user=request.user)
    if request.method == 'POST':
        tirkeme.delete()
        return redirect('regproje:tirkemeler_list')
    return render(request, 'regproje/register/tirkemeler_confirm_delete.html', {'tirkeme': tirkeme})

@login_required
def menin_dolboorum(request):
    user = request.user
    user_projects = Dolboor.objects.filter(user=user)
    negizgimaalymat = Negizgimaalymat.objects.filter(user=user)
    kenenmaalymat = Kenenmaalymat.objects.filter(user=user)
    iskeashyruuplany = Iskeashyruuplany.objects.filter(user=user)
    dolboordundudjeti = Dolboordundudjeti.objects.filter(user=user)
    dolboordunkomandasy = Dolboordunkomandasy.objects.filter(user=user)
    baaloo_turuktuuluk = Baaloo_turuktuuluk.objects.filter(user=user).first()
    tirkemeler = Tirkemeler.objects.filter(user=user)

    context = {
        'user_projects': user_projects,
        'negizgimaalymat': negizgimaalymat,
        'kenenmaalymat': kenenmaalymat,
        'iskeashyruuplany': iskeashyruuplany,
        'dolboordundudjeti': dolboordundudjeti,
        'dolboordunkomandasy': dolboordunkomandasy,
        'baaloo_turuktuuluk': baaloo_turuktuuluk,
        'tirkemeler': tirkemeler,

        'dolboor_kayit_var': user_projects.exists(),
        'negizgimaalymat_kayit_var': negizgimaalymat.exists(),
        'kenenmaalymat_kayit_var': kenenmaalymat.exists(),
        'iskeashyruuplany_kayit_var': iskeashyruuplany.exists(),
        'dolboordundudjeti_kayit_var': dolboordundudjeti.exists(),
        'dolboordunkomandasy_kayit_var': dolboordunkomandasy.exists(),
        'baaloo_turuktuuluk_kayit_var': baaloo_turuktuuluk is not None,
        'tirkemeler_kayit_var': tirkemeler.exists()
    }
    return render(request, 'regproje/register/menin_dolboorum.html', context)


@login_required
def project_confirmation_view(request):
    dolboors = Dolboor.objects.all()

    if request.method == 'POST':
        dolboor_id = request.POST.get('dolboor_id')
        comment = request.POST.get('comment')
        applicant_user_id = request.POST.get('applicant_user_id')
        confirmation = 'confirmation' in request.POST

        dolboor = get_object_or_404(Dolboor, id=dolboor_id)

        # Eğer form gönderilmişse bir Project_confirmation kaydı oluşturuyoruz
        Project_confirmation.objects.create(
            user=request.user,
            dolboor=dolboor,
            comment=comment,
            confirmation=confirmation,
            applicant_user_id=applicant_user_id
        )

        return redirect('regproje:index')  # Aynı view'a yönlendirme

    context = {
        'dolboors': dolboors,
    }

    return render(request, 'regproje/register/index.html', context)