from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/standings/', views.standings, name='standings'),
    path('/<str:team>/', views.team, name='team'),
    # path('/<str:team>/<str:player>/', views.player, name='player'),
]