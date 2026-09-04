from django.urls import path
from . import views

urlpatterns = [

    path('vhod/', views.auth_view, name='auth_view'),
    path('logout/', views.auth_view, name='logout'),  # выход
    path('tours/', views.tours_view, name='tours'),
    path('tours/<int:tour_id>/booking/', views.tour_booking, name='tour_booking'), # url для бронирования
]
