from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_articoli, name='articoli'),
    path('<str:titolo_articolo>/', views.dettagli_articolo, name='articolo'),
    # path('<str:campaign_name>/impostazioni/', views.settings, name='impostazioni_campagna'),
    # path('<str:campaign_name>/gioca/', views.play, name='impostazioni_campagna'),
]