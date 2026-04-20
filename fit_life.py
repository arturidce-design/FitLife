import sys
sys.stdout.reconfigure(encoding="utf-8")


WATER_PER_KG = 30
LITERS_IN_ML = 1000


def calculate_bmi(weight, height):
    """Калькулятор индекса массы тела (BMI)."""
    return round(weight / (height ** 2), 1)


def calculate_water_norm(weight):
    """Калькулятор нормы воды в организме."""
    water_ml = weight * WATER_PER_KG
    water_l = round(water_ml / LITERS_IN_ML, 1)
    return water_l


print("Добро пожаловать в калькулятор здоровья FitLife!")

#  Получение данных от пользователя.
user_name = input("Введите ваше имя: ").capitalize()
user_age = int(input(f"Здравствуйте, {user_name}! Введите ваш возраст: "))
user_weight = float(input("Введите ваш вес в килограммах: "))
user_height = float(input("Введите ваш рост в метрах: "))

#  Вывод результатов.
print(
    f"\n{'=' * 40}\n"
    f"Спасибо, {user_name}! Вот ваши результаты:\n"
    f"Ваш Индекс Массы Тела (BMI): {calculate_bmi(user_weight, user_height)}\n"
    f"Рекомендуемое количество воды в день: \
        {calculate_water_norm(user_weight)} литров\n"
    f"\n{'=' * 40}\n"
    "Благодарим за использование калькулятора здоровья FitLife! \
    Берегите себя и будьте здоровы!"
)
