def sort_by_age(data, reverse=False):
    """
    Сортирует студентов по возрасту.

    Args:
        data (list): Список словарей с данными студентов
        reverse (bool): По убыванию если True

    Returns:
        list: Отсортированный список
    """
    return sorted(data, key=lambda s: s["age"], reverse=reverse)


def avg_grade(student):
    """
    Вычисляет средний балл студента.

    Args:
        student (dict): Данные студента с ключом 'grades'

    Returns:
        float: Средний балл
    """
    grades = student["grades"]
    return sum(grades) / len(grades)


def best_students(data, top=3):
    """
    Находит лучших студентов по среднему баллу.

    Args:
        data (list): Список студентов
        top (int): Количество лучших

    Returns:
        list: Список лучших студентов
    """
    sorted_data = sorted(data, key=lambda x: avg_grade(x), reverse=True)
    return sorted_data[:top]


def unique_names(data):
    """
    Извлекает уникальные имена студентов.

    Args:
        data (list): Список студентов

    Returns:
        set: Множество уникальных имен
    """
    return set(s["name"] for s in data)