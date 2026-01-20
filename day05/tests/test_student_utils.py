import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.student_utils import sort_by_age, avg_grade, best_students, unique_names


def test_avg_grade():
    """Тест средней оценки."""
    student = {"grades": [5, 4, 3]}
    assert avg_grade(student) == 4.0


def test_sort_by_age():
    """Тест сортировки по возрасту."""
    students = [
        {"name": "А", "age": 20},
        {"name": "Б", "age": 18}
    ]
    sorted_students = sort_by_age(students)
    assert sorted_students[0]["age"] == 18


def test_best_students():
    """Тест лучших студентов."""
    students = [
        {"name": "С1", "grades": [3, 3, 3]},
        {"name": "С2", "grades": [5, 5, 5]}
    ]
    best = best_students(students, top=1)
    assert best[0]["name"] == "С2"


def test_unique_names():
    """Тест уникальных имен."""
    students = [
        {"name": "Иван", "age": 20},
        {"name": "Иван", "age": 21}
    ]
    unique = unique_names(students)
    assert len(unique) == 1
    assert "Иван" in unique