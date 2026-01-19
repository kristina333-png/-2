import json

students = [
    {"name": "Иван", "age": 18, "grades": [5, 4, 3, 5, 4]},
    {"name": "Мария", "age": 19, "grades": [5, 5, 4, 5, 5]},
    {"name": "Алексей", "age": 20, "grades": [4, 4, 3, 5, 4]},
    {"name": "Анна", "age": 18, "grades": [5, 5, 5, 4, 5]},
    {"name": "Дмитрий", "age": 21, "grades": [3, 4, 4, 3, 4]},
    {"name": "Екатерина", "age": 19, "grades": [5, 4, 5, 5, 4]},
    {"name": "Сергей", "age": 22, "grades": [4, 3, 4, 4, 3]},
    {"name": "Ольга", "age": 18, "grades": [5, 5, 5, 5, 5]},
    {"name": "Павел", "age": 20, "grades": [4, 4, 4, 4, 4]},
    {"name": "София", "age": 19, "grades": [5, 4, 5, 4, 5]},
    {"name": "Иван", "age": 21, "grades": [4, 3, 4, 4, 3]},
    {"name": "Анна", "age": 20, "grades": [5, 4, 5, 5, 4]}
]

with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

