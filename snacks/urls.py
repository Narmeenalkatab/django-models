from django.urls import path
from .views import SnackListView,SnackDetailsView

urlpatterns = [
# path('',HomeView.as_view(), name='home'),
path('',SnackListView.as_view(), name='home'),
# path('snacksdetails/',SnackDetailsView.as_view(), name='snack_details'),
path('snacks/<pk>/',SnackDetailsView.as_view(), name='snack_details')




]