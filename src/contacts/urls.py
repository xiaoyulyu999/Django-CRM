from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path('', views.contacts_list_view, name='list_contacts'),
]
