from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from regproje.models import Project_confirmation

def index(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    list_project_confirmation = Project_confirmation.objects.all()

    context = {
        'list_project_confirmation' : list_project_confirmation,
    }

    return render(request, "main/index.html", context)