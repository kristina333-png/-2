import os
import tempfile

numbers = []
with open('io_tasks/numbers.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:  
            try:
                numbers.append(float(line))
            except ValueError:
                pass


if numbers:
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)


    with tempfile.NamedTemporaryFile(mode='w', delete=False,encoding='utf-8') as tmp:
        tmp.write(f"Минимум: {minimum}\n")
        tmp.write(f"Максимум: {maximum}\n")
        tmp.write(f"Среднее: {average}\n")
        tmp_path = tmp.name


    os.replace(tmp_path, 'result.txt')