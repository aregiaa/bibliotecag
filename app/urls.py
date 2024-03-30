from django.urls import path
from .views import *

urlpatterns = [
    path('', ConsultaView.as_view(), name='index'),
]