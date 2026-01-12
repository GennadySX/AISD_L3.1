#!/usr/bin/env python3
"""
Запуск интерактивной программы AISD_L3
Используйте: python3 run.py
или просто: ./run.py (если разрешены права на выполнение)
"""

import subprocess
import sys
import os

# Получить абсолютный путь к папке проекта
project_dir = os.path.dirname(os.path.abspath(__file__))

# Запустить main.py
main_file = os.path.join(project_dir, 'main.py')

if not os.path.exists(main_file):
    print(f"Ошибка: файл {main_file} не найден")
    sys.exit(1)

# Запустить main.py с текущим интерпретатором Python
sys.exit(subprocess.call([sys.executable, main_file]))

