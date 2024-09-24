from django.urls import path
from . import views


urlpatterns = [
    path('district', views.add_district, name='district')
]
