from django.urls import path
from .views import HomeView,SnackListView,SnackDetailsView

urlpatterns = [

    path('',HomeView.as_view(), name='home'),
    path('things/',SnackListView.as_view(), name='things'),
    path('things/<pk>/',SnackDetailsView.as_view(), name='thing_details')
]