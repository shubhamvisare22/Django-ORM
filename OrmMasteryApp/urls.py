from django.urls import path
from . import views

urlpatterns = [
    path("orm/",views.list_view, name="list_view")
]
