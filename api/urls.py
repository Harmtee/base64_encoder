from django.urls import path
from .views import EncodeView, DecodeView

urlpatterns = [
    path('encode/', EncodeView.as_view(), name='encode'),
    path('decode/', DecodeView.as_view(), name='decode'),
]
