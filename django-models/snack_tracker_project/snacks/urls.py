from django.urls import path 
from .views import SnackListView,SnackDetailView


urlpatterns = [
  path ('snack-list' , SnackListView.as_view(),name = 'snack_list'),
  path ('snack-detail/<int:pk>' , SnackDetailView.as_view(),name = 'snack_detail')

       ]