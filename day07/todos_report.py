import json


def main():
    """
    Анализируем задачи и создаем отчет.
    """
    print(" Анализируем задачи...")

    try:

        with open("data/todos.json", "r", encoding="utf-8") as f:
            todos = json.load(f)

        if not todos:
            print("Нет данных для анализа")
            return

        print(f" Загружено {len(todos)} задач")


        total = len(todos)
        completed = sum(1 for task in todos if task['completed'])
        not_completed = total - completed


        user_stats = {}
        for task in todos:
            user_id = task['userId']
            if user_id not in user_stats:
                user_stats[user_id] = {'всего': 0, 'выполнено': 0}

            user_stats[user_id]['всего'] += 1
            if task['completed']:
                user_stats[user_id]['выполнено'] += 1


        top_users = []
        for user_id, stats in user_stats.items():
            top_users.append({
                'id': user_id,
                'выполнено': stats['выполнено'],
                'всего': stats['всего']
            })


        top_users.sort(key=lambda x: x['выполнено'], reverse=True)


        print("\n" + "=" * 50)
        print("ОТЧЕТ ПО ЗАДАЧАМ")
        print("=" * 50)

        print(f"\n ОБЩАЯ СТАТИСТИКА:")
        print(f"  Всего задач: {total}")
        print(f"  Выполнено: {completed} ({completed / total * 100:.1f}%)")
        print(f"  Не выполнено: {not_completed}")

        print(f"\n👥 ПОЛЬЗОВАТЕЛИ:")
        print(f"  Всего пользователей: {len(user_stats)}")

        print(f"\n🏆 ТОП-3 ПОЛЬЗОВАТЕЛЯ:")
        for i, user in enumerate(top_users[:3], 1):
            print(f"  {i}. Пользователь {user['id']}:")
            print(f"     Выполнено задач: {user['выполнено']}")
            print(f"     Всего задач: {user['всего']}")
            print(f"     Процент выполнения: {user['выполнено'] / user['всего'] * 100:.1f}%")

        print("\n" + "=" * 50)
        print("Отчет готов!")

    except FileNotFoundError:
        print("Файл data/todos.json не найден!")
        print("   Сначала запусти fetch_todos.py")
    except Exception as e:
        print(f" Ошибка: {e}")


if __name__ == "__main__":
    main()