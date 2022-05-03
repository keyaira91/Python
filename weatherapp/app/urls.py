from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]