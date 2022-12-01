from django.urls import path
from .views import*
urlpatterns = [
    path('',index,name='anasayfa'),
    path('urunler/',urunler,name='urunler')
]
