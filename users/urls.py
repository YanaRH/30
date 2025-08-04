from django.shortcuts import render, get_object_or_404
from .models import User  # Убедитесь, что модель User импортирована
from django.http import JsonResponse

def user_list(request):
    users = User.objects.all()  # Получаем всех пользователей
    user_data = [{"id": user.id, "email": user.email, "phone": user.phone, "city": user.city} for user in users]
    return JsonResponse(user_data, safe=False)  # Возвращаем список пользователей в формате JSON

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)  # Получаем пользователя по первичному ключу
    user_data = {
        "id": user.id,
        "email": user.email,
        "phone": user.phone,
        "city": user.city,
    }
    return JsonResponse(user_data)  # Возвращаем данные пользователя в формате JSON


