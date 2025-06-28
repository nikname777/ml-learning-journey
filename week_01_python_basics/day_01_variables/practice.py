"""
Day 1: Variables and Basic Types in Python
Author: [Твое имя]
Date: [Сегодняшняя дата]
Goal: Master Python fundamentals for ML journey
"""

# My first step towards ML Engineering!
print("🚀 Starting my ML learning journey!")
print(f"Today is Day 1 of my 16-week transformation")

# TODO: Today's topics
# - Variables and data types
# - Basic operations
# - String formatting

"""
День 1: Переменные и базовые типы данных
========================================
Время изучения: 2 часа
"""

# ============================================
# ЧАСТЬ 3: ФОРМАТИРОВАНИЕ СТРОК (15 мин)
# ============================================

name = "Alice"
age = 30
height = 165.5

# Старый стиль (не рекомендуется)
old_style = "Name: %s, Age: %d" % (name, age)

# .format() метод
format_style = "Name: {}, Age: {}".format(name, age)
format_named = "Name: {n}, Age: {a}".format(n=name, a=age)

# f-строки (рекомендуется!) - Python 3.6+
f_string = f"Name: {name}, Age: {age}"
f_expression = f"In 10 years {name} will be {age + 10}"
f_format = f"Height: {height:.1f} cm"  # 1 знак после запятой

# Выравнивание в f-строках
product = "Apple"
price = 1.23
print(f"\n=== Форматирование ===")
print(f"{product:<10} ${price:>6.2f}")  # < выравнивание влево, > вправо
print(f"{product:^10} ${price:^6.2f}")  # ^ по центру
