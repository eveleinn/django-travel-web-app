# настраивает отображение моделей в админке Django
from django.contrib import admin
from .models import Tour, Booking


class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'duration', 'date', 'price')


admin.site.register(Tour, TourAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'phone_number')


admin.site.register(Booking, BookingAdmin)
