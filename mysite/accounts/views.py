from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Tour, Booking


def auth_view(request):
    # Обработка GET-запроса (выход)
    if request.method == 'GET' and 'logout' in request.GET:
        logout(request)
        messages.success(request, 'Вы успешно вышли из системы.')
        return redirect('auth_view')  # Перенаправляем на страницу входа

    # Обработка POST-запросов (вход и регистрация)
    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)  # если данные верны
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему.')
                return redirect('auth_view')
            else:
                messages.error(request, 'Неверный логин или пароль.')


        elif 'register' in request.POST:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()  # Сохраняем пользователя
                messages.success(request, 'Ваш аккаунт был успешно создан! Вы можете войти.')
                return redirect('auth_view')
            else:
                messages.error(request, 'Ошибка регистрации. Попробуйте снова.')
    return render(request, 'vhod.html')


def tours_view(request):
    tours = Tour.objects.all()  # Загружаем все туры из базы данных
    return render(request, '2.html', {'tours': tours})  # Передаем туры в шаблон


@login_required
def tour_booking(request, tour_id):
    tour = Tour.objects.get(id=tour_id)

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if phone_number:
            # Создаем запись о бронировании (если метод POST)
            booking = Booking(user=request.user, tour=tour, phone_number=phone_number)
            try:
                booking.save()
                messages.success(request,
                                 f'Вы успешно забронировали тур! Свяжитесь с нами по номеру телефона +79376743333')
            except Exception as e:
                messages.error(request, 'Ошибка при сохранении бронирования. Попробуйте снова.')
        else:
            messages.error(request, 'Пожалуйста, введите номер телефона.')

        return redirect('tour_booking', tour_id=tour.id)  # Перенаправление на страницу с сообщениями
    return redirect('tours')  # Перенаправление на страницу всех туров, если метод не POST
