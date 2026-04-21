import sys

sys.stdout.reconfigure(encoding="utf-8")


WATER_PER_KG = 30
LITERS_IN_ML = 1000
OUTPUT_SEPARATOR = "\n" + "=" * 40 + "\n"


def calculate_bmi(weight, height):
    """Калькулятор индекса массы тела (BMI)."""
    return round(weight / (height ** 2), 1)


def calculate_water_norm(weight):
    """Калькулятор нормы воды в организме."""
    water_ml = weight * WATER_PER_KG
    return round(water_ml / LITERS_IN_ML, 1)


print("Добро пожаловать в калькулятор здоровья FitLife!")

#  Получение данных от пользователя.
user_name = input("Введите ваше имя: ").title()
try:
    user_age = int(input(f"Здравствуйте, {user_name}! Введите Ваш возраст: "))
except ValueError:
    user_age = int(input("Ошибка. Введите корректное число для возраста: "))
try:
    user_weight = float(input("Введите ваш вес в килограммах: "))
except ValueError:
    user_weight = float(input("Ошибка. Введите корректное число для веса: "))
try:
    user_height = float(input("Введите ваш рост в метрах: "))
except ValueError:
    user_height = float(input("Ошибка. Введите корректное число для роста: "))

bmi = calculate_bmi(user_weight, user_height)
water_norm = calculate_water_norm(user_weight)

#  Вывод результатов.
print(OUTPUT_SEPARATOR)
print(f"Спасибо, {user_name}! Вот Ваши результаты:")
print(
    f"Ваш Индекс Массы Тела (BMI): {bmi}",
)
print(
    f"Рекомендуемое количество воды в день: {water_norm} литров",
)
print(OUTPUT_SEPARATOR)
print(
    "Благодарим за использование калькулятора здоровья FitLife!\n",
    "Берегите себя и будьте здоровы!",
)
