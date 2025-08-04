class Product:
    """Класс для представления продукта."""
    def __init__(self, title):
        self.title = title

def create_product(instance):
    """Создаем продукт."""
    title_product = instance.paid_course if instance.paid_course else instance.paid_lesson
    product = Product(title_product)
    return product

def convert_rub_to_dol(amount, conversion_rate=0.013):  # Примерный курс рубля к доллару
    """Конвертируем рубли в доллары."""
    result = amount * conversion_rate
    return result

def create_price(amount):
    """Создаем цену."""
    # Здесь можно добавить логику для обработки цены
    return amount  # Возвращаем переданную сумму без изменений

def create_session(price):
    """Создаем сессию."""
    # Здесь можно добавить логику для создания сессии
    return {"id": "session_id", "url": "https://example.com"}  # Возвращаем фиктивные данные

# Пример использования
class PaymentInstance:
    """Класс для представления экземпляра платежа."""
    def __init__(self, paid_course=None, paid_lesson=None):
        self.paid_course = paid_course
        self.paid_lesson = paid_lesson

# Создаем экземпляр платежа
payment_instance = PaymentInstance(paid_course="Курс по программированию")

# Создаем продукт
product = create_product(payment_instance)
print(f"Создан продукт: {product.title}")

# Конвертируем рубли в доллары
amount_rub = 1000  # Сумма в рублях
amount_usd = convert_rub_to_dol(amount_rub)
print(f"{amount_rub} рублей = {amount_usd:.2f} долларов")

# Создаем цену
price = create_price(amount_usd)
print(f"Цена: {price:.2f} долларов")

# Создаем сессию
session = create_session(price)
print(f"Создана сессия: ID = {session['id']}, URL = {session['url']}")



