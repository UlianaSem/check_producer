from main.apps import MainConfig
from django.urls import path

from main.views import CheckCreateAPIView

app_name = MainConfig.name

urlpatterns = [
    path('checks/', CheckCreateAPIView.as_view(), name='add_check'),
]
