import json

with open('io_tasks/students.json', 'r', encoding='utf-8') as f:
    original = json.load(f)
    original_count = len(original)

updated = original.copy()
updated.append({
    "name": "Екатерина",
    "age": 19,
    "grades": [5, 5, 4, 5, 5]
})

with open('students_updated.json', 'w', encoding='utf-8') as f:
    json.dump(updated, f, ensure_ascii=False, indent=2)

with open('io_tasks/students.json', 'r', encoding='utf-8') as f:
    check = json.load(f)

if len(check) == original_count:
    print(" Исходный файл не изменен")
else:
    print("Ошибка: исходный файл изменился")

