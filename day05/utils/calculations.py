def add(a, b):
    """Сложение двух чисел."""
    return a + b


def sub(a, b):
    """Вычитание двух чисел."""
    return a - b


def mul(a, b):
    """Умножение двух чисел."""
    return a * b


def div(a, b):
    """Деление двух чисел."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль недопустимо!")
        return None


def is_prime(n):
    """
    Проверяет, является ли число простым.

    Args:
        n (int): Число для проверки

    Returns:
        bool: True если число простое, иначе False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start=2, end=100):
    """
    Находит простые числа в диапазоне.

    Args:
        start (int): Начало диапазона
        end (int): Конец диапазона

    Returns:
        list: Список простых чисел
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes