from django.urls import path
from . import views

urlpatterns = [
    path('<str:group_name>/',views.home,name='home'),
]
