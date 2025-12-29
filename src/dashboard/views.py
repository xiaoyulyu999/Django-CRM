from django.http import HttpResponse
from django.shortcuts import redirect


def dashboard_index(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/auth/google/login/")
    return HttpResponse("Hello, world. You're at the dashboard index.")
