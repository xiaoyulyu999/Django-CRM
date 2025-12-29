from django.shortcuts import redirect, render
from random import randint


def dashboard_index(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/auth/google/login/")

    my_value = str(request.user) + str(randint(1, 1000000))
    template_context = {
        "my_value": my_value,
        "not_actual_context": "now it's ready",
        "colors": ["red", "blue"],
    }
    return render(request, "dashboard/main.html", template_context)
