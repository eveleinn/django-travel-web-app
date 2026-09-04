from django import forms
from django.contrib.auth.models import User
from .models import Booking


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) # шифрование пароля


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tour', 'phone_number']

    phone_number = forms.CharField(max_length=20, required=True, label='Ваш номер телефона')
