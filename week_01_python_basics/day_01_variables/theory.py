# ============================================
# ЧАСТЬ 1: ПЕРЕМЕННЫЕ И БАЗОВЫЕ ТИПЫ (30 мин)
# ============================================

# 1.1 Что такое переменная?
# Переменная - это именованная область памяти для хранения данных

# Создание переменных
name = "Valeriy"  # строка (str)
age = 25  # целое число (int)
height = 175.5  # дробное число (float)
is_student = True  # булево значение (bool)

# Python - язык с динамической типизацией
# Тип определяется автоматически
print(f"Тип name: {type(name)}")
print(f"Тип age: {type(age)}")
print(f"Тип height: {type(height)}")
print(f"Тип is_student: {type(is_student)}")

# 1.2 Правила именования переменных
# ✅ Можно:
user_name = "John"  # snake_case (рекомендуется в Python)
userName = "John"  # camelCase (не рекомендуется)
_private = 42  # начинается с подчеркивания
name2 = "Alice"  # содержит цифры

# ❌ Нельзя:
# 2name = "Bob"          # начинается с цифры
# user-name = "Bob"      # содержит дефис
# class = "Math"         # зарезервированное слово

# 1.3 Числовые типы
# Целые числа (int) - любой размер!
small_number = 42
big_number = 1234567890123456789012345678901234567890
negative = -100

# Дробные числа (float)
pi = 3.14159
scientific = 1.23e-4  # научная нотация: 0.000123
infinity = float('inf')  # бесконечность

# Операции с числами
a, b = 10, 3
print(f"\n=== Арифметические операции ===")
print(f"{a} + {b} = {a + b}")  # сложение
print(f"{a} - {b} = {a - b}")  # вычитание
print(f"{a} * {b} = {a * b}")  # умножение
print(f"{a} / {b} = {a / b}")  # деление (всегда float)
print(f"{a} // {b} = {a // b}")  # целочисленное деление
print(f"{a} % {b} = {a % b}")  # остаток от деления
print(f"{a} ** {b} = {a ** b}")  # возведение в степень

# 1.4 Строки (str)
# Создание строк
single_quotes = 'Hello'
double_quotes = "World"
multi_line = """Это
многострочная
строка"""

# Экранирование
escaped = "Он сказал: \"Привет!\""
path = "C:\\Users\\Name\\file.txt"
raw_string = r"C:\Users\Name\file.txt"  # raw строка

# Конкатенация и повторение
greeting = "Hello" + " " + "World"
repeated = "Ha" * 3  # "HaHaHa"

# 1.5 Булевы значения (bool)
is_true = True
is_false = False

# Операторы сравнения
x, y = 5, 10
print(f"\n=== Операторы сравнения ===")
print(f"{x} > {y} = {x > y}")  # больше
print(f"{x} < {y} = {x < y}")  # меньше
print(f"{x} >= {y} = {x >= y}")  # больше или равно
print(f"{x} <= {y} = {x <= y}")  # меньше или равно
print(f"{x} == {y} = {x == y}")  # равно
print(f"{x} != {y} = {x != y}")  # не равно

# Логические операторы
print(f"\n=== Логические операторы ===")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# ============================================
# ЧАСТЬ 2: ПРЕОБРАЗОВАНИЕ ТИПОВ (15 мин)
# ============================================

# Явное преобразование
num_str = "123"
num_int = int(num_str)  # строка в число
num_float = float(num_str)  # строка в дробное

age = 25
age_str = str(age)  # число в строку

# Осторожно с преобразованием!
# int("123.45")  # Ошибка! Нельзя напрямую
float_str = "123.45"
result = int(float(float_str))  # Сначала в float, потом в int

# Проверка типов
value = "42"
print(f"\n=== Проверка типов ===")
print(f"isinstance(value, str) = {isinstance(value, str)}")
print(f"isinstance(value, int) = {isinstance(value, int)}")

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

# ============================================
# ЧАСТЬ 4: NONE И ОСОБЫЕ ЗНАЧЕНИЯ (10 мин)
# ============================================

# None - отсутствие значения
result = None
print(f"\nresult is None: {result is None}")


# None часто используется как значение по умолчанию
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"


# Проверка на None
# ✅ Правильно
if result is None:
    print("Result is None")

# ❌ Неправильно (но работает)
if result == None:
    print("Result is None")

# ============================================
# ПРАКТИЧЕСКИЕ УПРАЖНЕНИЯ (45 мин)
# ============================================

print("\n" + "=" * 50)
print("ПРАКТИЧЕСКИЕ УПРАЖНЕНИЯ")
print("=" * 50)

# Упражнение 1: Калькулятор ИМТ
print("\n📝 Упражнение 1: Калькулятор ИМТ")
# TODO: Создайте переменные weight (вес в кг) и height (рост в метрах)
# Вычислите ИМТ по формуле: weight / (height ** 2)
# Выведите результат с 2 знаками после запятой

# Ваш код здесь:
weight = 75  # кг
height_m = 1.75  # метры
bmi = weight / (height_m ** 2)
print(f"Ваш ИМТ: {bmi:.2f}")

# Упражнение 2: Работа со строками
print("\n📝 Упражнение 2: Форматирование данных")
# TODO: Создайте переменные для имени, фамилии и возраста
# Создайте строку в формате: "Фамилия, И. (возраст лет)"

# Ваш код здесь:
first_name = "Иван"
last_name = "Петров"
age = 28
formatted = f"{last_name}, {first_name[0]}. ({age} лет)"
print(formatted)

# Упражнение 3: Конвертер температуры
print("\n📝 Упражнение 3: Конвертер температуры")
# TODO: Конвертируйте температуру из Цельсия в Фаренгейт
# Формула: F = C * 9/5 + 32

# Ваш код здесь:
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Упражнение 4: Проверка типов
print("\n📝 Упражнение 4: Определение типа данных")


# TODO: Создайте функцию, которая принимает значение
# и возвращает его тип в читаемом формате

def get_type_info(value):
    """Возвращает информацию о типе значения"""
    type_name = type(value).__name__
    return f"Значение '{value}' имеет тип {type_name}"


# Тесты
print(get_type_info(42))
print(get_type_info(3.14))
print(get_type_info("Hello"))
print(get_type_info(True))
print(get_type_info(None))

# ============================================
# МИНИ-ТЕСТ (30 мин)
# ============================================

print("\n" + "=" * 50)
print("МИНИ-ТЕСТ: Проверь себя!")
print("=" * 50)

# Вопрос 1: Что выведет этот код?
x = 10
y = 3
result = x // y * y + x % y
print(f"\nВопрос 1: result = {result}")
# Подумай перед запуском! Ответ должен быть 10

# Вопрос 2: Какой тип у результата?
a = 10
b = 3
c = a / b
print(f"\nВопрос 2: type(c) = {type(c)}")
# Подсказка: деление всегда возвращает float

# Вопрос 3: Что произойдет?
num = int("3.14")  # Раскомментируй и проверь
# Ответ: ValueError, нужно сначала float("3.14"), потом int()

# Вопрос 4: Какое значение?
text = "Python" * 2
print(f"\nВопрос 4: text = {text}")

# Вопрос 5: True или False?
result = not (5 > 3 and 2 < 1)
print(f"\nВопрос 5: result = {result}")

# ============================================
# ДОМАШНЕЕ ЗАДАНИЕ
# ============================================

"""
ДОМАШНЕЕ ЗАДАНИЕ (выполни в отдельном файле day_01_homework.py):

1. Калькулятор скидок
   - Создай переменные: цена товара, процент скидки
   - Вычисли: сумму скидки, финальную цену
   - Выведи чек в формате:
     Товар: ______ 
     Цена: $XXX.XX
     Скидка: XX%
     Экономия: $XX.XX
     К оплате: $XXX.XX

2. Анализатор текста
   - Создай переменную с текстом (минимум 3 предложения)
   - Подсчитай и выведи:
     * Количество символов
     * Количество символов без пробелов
     * Количество слов (подсказка: split())
     * Средняя длина слова

3. Конвертер единиц
   Создай универсальный конвертер:
   - Мили в километры (1 миля = 1.60934 км)
   - Фунты в килограммы (1 фунт = 0.453592 кг)
   - Галлоны в литры (1 галлон = 3.78541 л)

4. Генератор паролей (простой)
   - Создай переменные: имя, год рождения, любимое число
   - Сгенерируй 3 варианта паролей используя эти данные
   - Пример: Ivan1995!42, 1995_Ivan_42, Iv42an1995

5. Бонус: Мини-игра
   - Создай переменную с "секретным" числом
   - Создай переменные с тремя попытками угадать
   - Для каждой попытки выведи "Горячо" если разница < 10,
     "Тепло" если < 20, иначе "Холодно"
"""

print("\n" + "=" * 50)
print("🎯 Отличная работа! Теперь выполни домашнее задание")
print("📝 Создай файл day_01_homework.py в той же папке")
print("💾 Не забудь закоммитить: git commit -m 'Complete day 1 exercises'")
print("=" * 50)