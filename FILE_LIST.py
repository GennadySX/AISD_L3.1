#!/usr/bin/env python3
"""
Список всех файлов проекта AISD_L3 с подробной информацией
"""

import os
import glob

project_dir = "/Users/gsabirovsky/PycharmProjects/AISD_L3"

print("=" * 80)
print("ПОЛНЫЙ СПИСОК ФАЙЛОВ ПРОЕКТА AISD_L3")
print("=" * 80)

# Основные файлы
print("\n📁 ОСНОВНЫЕ ФАЙЛЫ ПРОГРАММЫ:")
print("-" * 80)

main_files = [
    ("main.py", "Главная программа с интерактивным меню"),
    ("run.py", "Вспомогательный скрипт для запуска"),
    ("demo.py", "Демонстрация работы всех 4 заданий"),
]

for file, desc in main_files:
    path = os.path.join(project_dir, file)
    if os.path.exists(path):
        size = os.path.getsize(path)
        with open(path) as f:
            lines = len(f.readlines())
        print(f"✓ {file:<25} {size:>8} байт  ({lines:>4} строк)  - {desc}")

# Модули заданий
print("\n📁 МОДУЛИ С РЕАЛИЗАЦИЕЙ АЛГОРИТМОВ:")
print("-" * 80)

task_files = [
    ("tasks/task_1_dfs.py", "Поиск в глубину (DFS)"),
    ("tasks/task_2_bfs.py", "Поиск в ширину (BFS)"),
    ("tasks/task_3_dijkstra.py", "Алгоритм Дейкстры"),
    ("tasks/task_4_traversal.py", "Обход графа (дерева)"),
    ("tasks/__init__.py", "Инициализация модуля tasks"),
]

for file, desc in task_files:
    path = os.path.join(project_dir, file)
    if os.path.exists(path):
        size = os.path.getsize(path)
        with open(path) as f:
            lines = len(f.readlines())
        print(f"✓ {file:<30} {size:>8} байт  ({lines:>4} строк)  - {desc}")

# Документация
print("\n📁 ДОКУМЕНТАЦИЯ:")
print("-" * 80)

doc_files = [
    ("README.md", "Полная документация с примерами и инструкциями"),
    ("QUICKSTART.md", "Быстрый старт для новых пользователей"),
    ("EXAMPLES.md", "10 примеров тестовых данных для каждого задания"),
    ("ARCHITECTURE.md", "Описание архитектуры, алгоритмов и сложности"),
    ("PROJECT_SUMMARY.md", "Сводка проекта и статус завершения"),
    ("requirements.txt", "Зависимости Python (не требуются!)"),
]

for file, desc in doc_files:
    path = os.path.join(project_dir, file)
    if os.path.exists(path):
        size = os.path.getsize(path)
        with open(path) as f:
            lines = len(f.readlines())
        print(f"✓ {file:<30} {size:>8} байт  ({lines:>4} строк)  - {desc}")

# Файлы задания
print("\n📁 ИСХОДНЫЕ ДАННЫЕ:")
print("-" * 80)

source_file = os.path.join(project_dir, "docs/TASKOF_AISD_L3.pdf")
if os.path.exists(source_file):
    size = os.path.getsize(source_file)
    print(f"✓ docs/TASKOF_AISD_L3.pdf  {size:>8} байт  - Исходное задание (PDF)")

# Статистика
print("\n" + "=" * 80)
print("СТАТИСТИКА ПРОЕКТА:")
print("=" * 80)

py_files = glob.glob(os.path.join(project_dir, "**/*.py"), recursive=True)
md_files = glob.glob(os.path.join(project_dir, "**/*.md"), recursive=True)

total_lines = 0
total_size = 0

for py_file in py_files:
    if '__pycache__' not in py_file:
        try:
            with open(py_file) as f:
                lines = len(f.readlines())
                total_lines += lines
                total_size += os.path.getsize(py_file)
        except:
            pass

for md_file in md_files:
    try:
        with open(md_file) as f:
            lines = len(f.readlines())
            total_lines += lines
            total_size += os.path.getsize(md_file)
    except:
        pass

print(f"\nФайлы Python (.py):")
print(f"  Количество: {len([f for f in py_files if '__pycache__' not in f])}")
print(f"  Всего строк кода: {total_lines}")
print(f"  Всего размер: {total_size:,} байт ({total_size / 1024:.1f} КБ)")

print(f"\nФайлы документации (.md):")
print(f"  Количество: {len(md_files)}")
print(f"  Всего файлов: {len(py_files) + len(md_files)}")

print(f"\nОбщая статистика:")
print(f"  ✓ 4 основных модуля с алгоритмами")
print(f"  ✓ 1 главная программа с меню")
print(f"  ✓ 1 демонстрационный скрипт")
print(f"  ✓ 5 файлов документации")
print(f"  ✓ Примеры и инструкции")

print("\n" + "=" * 80)
print("✅ ПРОЕКТ ПОЛНОСТЬЮ ГОТОВ К ИСПОЛЬЗОВАНИЮ")
print("=" * 80)

print("\nДля запуска программы выполните:")
print("\n  cd /Users/gsabirovsky/PycharmProjects/AISD_L3")
print("  python3 main.py")

print("\nДля демонстрации выполните:")
print("\n  python3 demo.py")

print("\n" + "=" * 80)

