from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to="lms/courses", verbose_name="Превью", blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата последнего обновления")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец", related_name="owned_courses")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['-last_update_date', 'title']

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    preview = models.ImageField(upload_to="lms/lessons", verbose_name="Превью", blank=True, null=True)
    url = models.URLField(max_length=200, verbose_name="Ссылка на видео", blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец", related_name="owned_lessons")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['title']

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name="subscriptions")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name="subscriptions")
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'course')
        ordering = ['-subscribed_at']

    def __str__(self):
        return f"{self.user} подписан на {self.course}"


class Payment(models.Model):
    date = models.DateField(verbose_name="Дата платежа")
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма платежа")
    category = models.CharField(max_length=100, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")
    card_number = models.CharField(max_length=20, verbose_name="Номер карты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.category}"





