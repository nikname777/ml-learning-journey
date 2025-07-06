"""
Day 1: Variables and Basic Types in Python
Author: [Твое имя]
Date: [Сегодняшняя дата]
Goal: Master Python fundamentals for ML journey
"""
from datetime import date

# My first step towards ML Engineering!
print("🚀 Starting my ML learning journey!")
print(f"Today is Day 1 of my 16-week transformation")

# TODO: Today's topics
# - Variables and data types
# - Basic operations
# - String formatting

# 1. Калькулятор скидок
#    - Создай переменные: цена товара, процент скидки
#    - Вычисли: сумму скидки, финальную цену
#    - Выведи чек в формате:
#      Товар: ______
#      Цена: $XXX.XX
#      Скидка: XX%
#      Экономия: $XX.XX
#      К оплате: $XXX.XX

# РЕШЕНИЕ

# good_price = 1000
# discount_percentage = 0.1
# discount_sum = good_price * discount_percentage
# final_price = good_price - discount_sum
#
# print("Товар: ______")
# print(f"Цена: ${good_price}")
# print(f"Скидка: ${int(discount_percentage*100)}%")
# print(f"Экономия: ${int(discount_sum)}")
# print(f"К оплате: ${int(final_price)}")


# 2. Анализатор текста
#    - Создай переменную с текстом (минимум 3 предложения)
#    - Подсчитай и выведи:
#      * Количество символов
#      * Количество символов без пробелов
#      * Количество слов (подсказка: split())
#      * Средняя длина слова

# РЕШЕНИЕ

# text = """
# Сегодня прекрасный день для прогулки в парке.
# Птицы поют, и солнце светит ярко на голубом небе.
# Многие люди вышли на улицу, чтобы насладиться хорошей погодой.
# """
#
# print(f"Кол-во символов: {len(text)}") #Кол-во символов
#
# #Кол-во символов без пробелов
# count = 0
# for item in text:
#     if item == ' ':
#         continue
#     else: count += 1
#
# print(f"Кол-во символов без пробелов: {count}")
#
# #Кол-во слов
# count_words = 0
# for item in text.split():
#     if item:
#         count_words += 1
# print(f"Кол-во слов: {count_words}")
#
# #Средняя длина слова
# length_word = 0
# count_words = 0
# avg_length_word = 0
# for item in text.split():
#     length_word += len(item)
#     count_words += 1
# avg_length_word = length_word / count_words
# print(f"Общая длина всех слов: {length_word}")
# print(f"Кол-во слов: {count_words}")
# print(f"Средняя длина слова: {avg_length_word}")

# 3. Конвертер единиц
#    Создай универсальный конвертер:
#    - Мили в километры (1 миля = 1.60934 км)
#    - Фунты в килограммы (1 фунт = 0.453592 кг)
#    - Галлоны в литры (1 галлон = 3.78541 л)

# miles_to_km = input("Перевести мили в километры: ")
# funds_to_kg = input("Перевести фунты в килограммы: ")
# gallons_to_litres = input("Перевести галлоны в литры: ")
#
# if miles_to_km:
#     print(f"{miles_to_km} миль равно {miles_to_km * 1.60934} километров")
# elif funds_to_kg:
#     print(f"{funds_to_kg} фунтов равно {funds_to_kg * 0.453592} килограммов")
# else: print(f"{gallons_to_litres} галлонов равно {gallons_to_litres * 3.78541} литров")

# print("Выберите вариант перевода:")
# print("1. Перевести мили в километры")
# print("2. Перевести фунты в килограммы")
# print("3. Перевести галлоны в литры")
#
# выбор = input("Введите номер варианта (1, 2 или 3): ")
#
# if выбор == "1":
#     мили = float(input("Введите количество миль: "))
#     километры = мили * 1.60934
#     print(f"{мили} миль = {километры} километров")
# elif выбор == "2":
#     фунты = float(input("Введите количество фунтов: "))
#     килограммы = фунты * 0.453592
#     print(f"{фунты} фунтов = {килограммы} килограммов")
# elif выбор == "3":
#     галлоны = float(input("Введите количество галлонов: "))
#     литры = галлоны * 3.78541
#     print(f"{галлоны} галлонов = {литры} литров")
# else:
#     print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")


# Генератор паролей (простой)
#    - Создай переменные: имя, год рождения, любимое число
#    - Сгенерируй 3 варианта паролей используя эти данные
#    - Пример: Ivan1995!42, 1995_Ivan_42, Iv42an1995

#РЕШЕНИЕ

# name = "Valeriy"
# date_of_birth = "1982"
# favourite_number = '12'
#
# print(name + date_of_birth + "!" + favourite_number)
# print(date_of_birth + "_" + name + "_" + favourite_number)
# print(name[:2] + favourite_number + name[2:] + date_of_birth)


# Бонус: Мини-игра
#    - Создай переменную с "секретным" числом
#    - Создай переменные с тремя попытками угадать
#    - Для каждой попытки выведи "Горячо" если разница < 10,
#      "Тепло" если < 20, иначе "Холодно"


#РЕШЕНИЕ

# secret_num = int(input("Enter a number: "))
#
# if secret_num <= 10:
#     print("Горячо")
# elif secret_num > 10 and secret_num <= 20:
#     print("Тепло")
# else:
#     print("Холодно")