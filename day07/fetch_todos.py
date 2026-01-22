import requests
import json
import os


def main():
    """
    Главная функция для получения данных из API.
    """
    print(" Подключаемся к API...")

    url = "https://jsonplaceholder.typicode.com/todos"

    try:

        response = requests.get(url, timeout=10)


        if response.status_code != 200:
            print(f" Ошибка сервера: {response.status_code}")
            return


        todos = response.json()
        print(f" Получено {len(todos)} задач")


        if not os.path.exists("data"):
            os.makedirs("data")

        with open("data/todos.json", "w", encoding="utf-8") as f:
            json.dump(todos, f, indent=2, ensure_ascii=False)

        print(" Данные сохранены в data/todos.json")


        if todos:
            print(f"\nПример задачи:")
            print(f"  ID: {todos[0]['id']}")
            print(f"  Пользователь: {todos[0]['userId']}")
            print(f"  Заголовок: {todos[0]['title'][:50]}...")
            print(f"  Выполнено: {'Да' if todos[0]['completed'] else 'Нет'}")

    except requests.exceptions.Timeout:
        print("Таймаут: сервер не отвечает")
    except requests.exceptions.RequestException as e:
        print(f" Ошибка соединения: {e}")
    except Exception as e:
        print(f" Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()