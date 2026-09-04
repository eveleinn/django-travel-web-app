from django.db import models
from django.contrib.auth.models import User


class Tour(models.Model):
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100,
                                  choices=[('Низкая', 'Низкая'), ('Средняя', 'Средняя'), ('Высокая', 'Высокая')],
                                  default='Средняя')
    duration = models.IntegerField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def formatted_price(self):
        return f"{int(self.price):,}".replace(",", " ")  # с пробелами цена


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.tour.name} - {self.phone_number}"
