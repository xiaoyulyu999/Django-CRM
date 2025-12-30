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


def get_image(request, *args, **kwargs):
    """
    nginx - load folder -
    object storage - aws s3 - cloudflare r2 -
    django-storage
    whitenoise
    """
    pass