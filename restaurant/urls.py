from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('book', views.BookView.as_view(), name="book"),
    path('reservations', views.ReservationsView.as_view(), name="reservations"),
    path('menu', views.MenuView.as_view(), name="menu"),
    path('menu-item/<int:pk>', views.MenuView.as_view(), name="menu_item"),  
    path('bookings', views.bookings, name='bookings'), 
]