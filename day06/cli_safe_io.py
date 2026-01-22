
import argparse
import logging
import sys
import os
from safe_io import read_numbers_from_file, calculate_statistics


def setup_logging():
    """
    Настраиваем логирование.
    Логи будут и в файл, и в консоль.
    """

    if not os.path.exists("logs"):
        os.makedirs("logs")


    log_format = '%(asctime)s - %(levelname)s - %(message)s'

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler("logs/app.log", encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """
    Главная функция.
    """

    setup_logging()


    parser = argparse.ArgumentParser(description='Чтение чисел из файла')
    parser.add_argument('файл', help='Путь к файлу с числами')


    args = parser.parse_args()
    file_path = args.файл

    try:
        print(f"Читаем файл: {file_path}")
        print("-" * 40)


        numbers, read_stats = read_numbers_from_file(file_path)


        stats = calculate_statistics(numbers)


        print("\n РЕЗУЛЬТАТЫ:")
        print(f"Всего строк в файле: {read_stats['всего_строк']}")
        print(f"Успешно прочитано чисел: {read_stats['успешно']}")
        print(f"Пропущено строк (не числа): {read_stats['пропущено']}")
        print(f"Пустых строк: {read_stats['пустых_строк']}")

        if numbers:
            print(f"\nСтатистика чисел:")
            print(f"  Количество: {stats['количество']}")
            print(f"  Сумма: {stats['сумма']:.2f}")
            print(f"  Среднее: {stats['среднее']:.2f}")
            print(f"  Минимальное: {stats['мин']}")
            print(f"  Максимальное: {stats['макс']}")
        else:
            print("\n  В файле нет корректных чисел!")

        print(f"\n Готово! Логи сохранены в logs/app.log")

    except Exception as e:
        print(f"\n Ошибка: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()