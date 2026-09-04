from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('accounts/', include('accounts.urls')),  # Включаем маршруты для авторизации
    path('', lambda request: render(request, '1.html'), name='home'),  # Главная страница
    path('reviews/', lambda request: render(request, '3.html'), name='reviews'),
    path('contacts/', lambda request: render(request, '4.html'), name='contacts'),
    path('vhod/', lambda request: render(request, 'vhod.html'), name='vhod'),
    path('tours/', include('accounts.urls')),  # Туры через `accounts/urls`
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
