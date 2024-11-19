from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

def login_request(request):
    if request.user.is_authenticated:
        return redirect_based_on_group(request)

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_based_on_group(request)  # Киргенден кийин багытточу функция
        else:
            return render(request, "account/login.html", {
                "error": "аты же сырсөз туура эмес"
            })

    return render(request, "account/login.html")

def redirect_based_on_group(request):
    user = request.user
    if user.groups.filter(name='Кадро').exists():
        # "Кадро" группасын багыттоо
        return redirect('main:home')
    elif user.groups.filter(name='Комиссия').exists():
        # "Комиссия" группасын багытоо
        return redirect('regproje:index')
    else:
        # Эгер кирген юзер-аккаун бир группага мүчө эмес болсо бул жака багытталат
        return redirect('regproje:menin_dolboorum')

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'account/register.html', {"error": "бул колдонуучу-ат мурунтан эле бар"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'account/register.html', {"error": "бул эл.куржун мурунтан эле бар"})
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    user.save()
                    return redirect("account:login")

        else:
            return render(request, 'account/register.html', {"error":"Сыр сөз туура келбейт"})

    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("main:home")

@receiver(post_save, sender=User)
def add_user_to_applying_group(sender, instance, created, **kwargs):
    if created:
        # "Долбоорчулар" админ панелден бул группа мурдатан жасалышы-жаратылышы керек
        group, created = Group.objects.get_or_create(name='Долбоорчулар')
        instance.groups.add(group)