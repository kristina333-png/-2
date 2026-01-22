import logging
import traceback


def read_numbers_from_file(file_path):
    """
    Читает числа из файла.
    Возвращает список чисел и статистику.
    """

    logging.info(f"Начинаем читать файл: {file_path}")

    numbers = []
    stats = {
        "всего_строк": 0,
        "успешно": 0,
        "пропущено": 0,
        "пустых_строк": 0
    }

    try:

        with open(file_path, 'r', encoding='utf-8') as file:

            for line_num, line in enumerate(file, 1):
                stats["всего_строк"] += 1
                line = line.strip()


                if not line:
                    stats["пустых_строк"] += 1
                    continue


                try:
                    number = float(line)
                    numbers.append(number)
                    stats["успешно"] += 1
                except ValueError:

                    logging.warning(f"Строка {line_num}: '{line}' - не число, пропускаем")
                    stats["пропущено"] += 1

    except FileNotFoundError:

        logging.error(f"Файл {file_path} не найден!")
        raise
    except Exception as e:

        logging.error(f"Ошибка при чтении файла: {e}")
        logging.error(traceback.format_exc())
        raise

    logging.info(f"Файл прочитан. Найдено {len(numbers)} чисел")
    return numbers, stats


def calculate_statistics(numbers):
    """
    Считает статистику по числам.
    """
    if not numbers:
        return {
            "количество": 0,
            "сумма": 0,
            "среднее": 0,
            "мин": None,
            "макс": None
        }

    return {
        "количество": len(numbers),
        "сумма": sum(numbers),
        "среднее": sum(numbers) / len(numbers),
        "мин": min(numbers),
        "макс": max(numbers)
    }