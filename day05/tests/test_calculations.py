import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.calculations import add, sub, mul, div, is_prime, find_primes_in_range

def test_add():
    """Тест сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 1.5) == 4.0


def test_sub():
    """Тест вычитания."""
    assert sub(5, 3) == 2
    assert sub(10, -5) == 15
    assert sub(3.5, 1.5) == 2.0


def test_mul():
    """Тест умножения."""
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6
    assert mul(2.5, 2) == 5.0


def test_div():
    """Тест деления."""
    assert div(10, 2) == 5.0
    assert div(5, 2) == 2.5
    assert div(5, 0) is None


def test_is_prime():
    """Тест проверки простых чисел."""
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(13) is True


def test_find_primes_in_range():
    """Тест поиска простых чисел в диапазоне."""

    result = find_primes_in_range(1, 10)
    assert result == [2, 3, 5, 7]


    result = find_primes_in_range(7, 7)
    assert result == [7]





def test_is_prime_negative():
    """Тест на отрицательные числа."""
    assert is_prime(-5) is False
    assert is_prime(-1) is False


def test_find_primes_in_range_invalid():
    """Тест некорректного диапазона."""
    result = find_primes_in_range(10, 1)
    assert result == []