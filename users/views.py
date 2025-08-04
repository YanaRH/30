from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Payments

User  = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def payment_list(request):
    payments = Payments.objects.all()
    return render(request, 'users/payment_list.html', {'payments': payments})  # Исправлено на 'payment_list.html'


