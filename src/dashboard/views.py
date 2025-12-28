from django.http import HttpResponse


def dashboard_index(request):
    return HttpResponse("Hello, world. You're at the dashboard index.")
