from django.urls import path
from .views import get_license
from .views import PyInfoView


urlpatterns = [
    path("get-license", get_license, name="get-license"),
    path('', PyInfoView.as_view(), name='info'),
]