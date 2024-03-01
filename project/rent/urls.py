from django.urls import path
from rent.views import RentListView, RentDetailView, RentCreateView


urlpatterns = [
    path('', RentListView.as_view(), name='list-view-rent'),
    path('<int:pk>/', RentDetailView.as_view(), name = 'detail-view-rent'),
    path('create/', RentCreateView.as_view(), name = 'create-view-rent'),



]