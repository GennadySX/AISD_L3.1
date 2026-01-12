"""
AISD_L3: Интерактивная консольная программа для решения задач по алгоритмам
Автор: Студент
Дата: 2026

Программа реализует 4 задания по теории графов и алгоритмам:
1. Поиск в глубину (DFS)
2. Поиск в ширину (BFS)
3. Алгоритм Дейкстры
4. Обход графа (дерева)
"""

import sys
import os

# Добавить папку tasks в путь импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tasks'))

from tasks.task_1_dfs import run_task_1
from tasks.task_2_bfs import run_task_2
from tasks.task_3_dijkstra import run_task_3
from tasks.task_4_traversal import run_task_4


def print_menu():
    """Вывести главное меню"""
    print("\n" + "="*70)
    print("AISD_L3 - ИНТЕРАКТИВНАЯ ПРОГРАММА ДЛЯ РЕШЕНИЯ ЗАДАЧ ПО ГРАФАМ")
    print("="*70)
    print("\nДоступные задания:")
    print("  1 - Поиск в глубину (DFS)")
    print("  2 - Поиск в ширину (BFS)")
    print("  3 - Алгоритм Дейкстры")
    print("  4 - Обход графа (дерева)")
    print("  0 - Выход из программы")
    print("\n" + "-"*70)


def get_user_choice() -> str:
    """Получить выбор пользователя"""
    while True:
        try:
            choice = input("Выберите номер задания: ").strip()
            if choice in ['0', '1', '2', '3', '4']:
                return choice
            else:
                print("Ошибка: пожалуйста, выберите число от 0 до 4")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            sys.exit(0)
        except Exception as e:
            print(f"Ошибка: {e}")


def run_selected_task(choice: str):
    """Запустить выбранное задание"""
    tasks = {
        '1': ('Поиск в глубину (DFS)', run_task_1),
        '2': ('Поиск в ширину (BFS)', run_task_2),
        '3': ('Алгоритм Дейкстры', run_task_3),
        '4': ('Обход графа (дерева)', run_task_4),
    }

    if choice in tasks:
        task_name, task_func = tasks[choice]
        print(f"\n✓ Выбрано задание: {task_name}")
        try:
            task_func()
        except KeyboardInterrupt:
            print("\n\nЗадание прервано пользователем.")
        except Exception as e:
            print(f"\nОшибка при выполнении задания: {e}")

    input("\nНажмите Enter для возврата в главное меню...")


def main():
    """Главная функция программы"""
    print("\n" + "="*70)
    print("Добро пожаловать в AISD_L3!")
    print("="*70)

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == '0':
            print("\nСпасибо за использование программы! До свидания!")
            break

        run_selected_task(choice)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена пользователем.")
        sys.exit(0)
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)
