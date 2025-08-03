from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from lms.models import Payment, Subscription  # Замените lms на имя вашего приложения
from decimal import Decimal

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми платежами'

    def handle(self, *args, **options):
        # Получаем все подписки
        subscriptions = Subscription.objects.all()

        if not subscriptions.exists():
            self.stdout.write(self.style.ERROR('Нет доступных подписок для создания платежей.'))
            return

        # Данные для тестовых платежей
        payments_data = [
            {
                "date": "2023-01-15",
                "amount": Decimal("1500.00"),
                "category": "Образование",
                "description": "Оплата курса по программированию",
                "card_number": "1234-5678-9012-3456",
                "subscription": subscriptions[0]  # Привязываем к первой подписке
            },
            {
                "date": "2023-02-20",
                "amount": Decimal("2500.00"),
                "category": "Образование",
                "description": "Оплата курса по дизайну",
                "card_number": "2345-6789-0123-4567",
                "subscription": subscriptions[1] if len(subscriptions) > 1 else subscriptions[0]  # Привязываем к второй подписке, если она есть
            },
            {
                "date": "2023-03-10",
                "amount": Decimal("3000.00"),
                "category": "Образование",
                "description": "Оплата курса по маркетингу",
                "card_number": "3456-7890-1234-5678",
                "subscription": subscriptions[2] if len(subscriptions) > 2 else subscriptions[0]  # Привязываем к третьей подписке, если она есть
            },
        ]

        for payment_data in payments_data:
            # Создаем платеж
            payment, created = Payment.objects.get_or_create(
                date=parse_date(payment_data["date"]),
                amount=payment_data["amount"],
                category=payment_data["category"],
                description=payment_data["description"],
                card_number=payment_data["card_number"]
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создан платеж: {payment}'))
            else:
                self.stdout.write(f'Платеж уже существует: {payment}')


