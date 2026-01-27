score = 78
if score >= 90:
    print("5 (отлично)")
elif score >= 70:
    print("4 (хорошо)")
elif score >= 50:
    print("3 (удовлетворительно)")
else:
    print("2 (неуд)")

x = -3
if x > 0:
    print("Положительное")
elif x < 0:
    print("Отрицательное")
else:
    print("Ноль")

age = 15
if age < 7:
    print("Скидка 50%")
elif age < 18:
    print("Скидка 20%")
elif age >= 60:
    print("Скидка 30%")
else:
    print("Без скидки")

hour = 21
if 6 <= hour <= 11:
    print("Утро")
elif 12 <= hour <= 17:
    print("День")
elif 18 <= hour <= 22:
    print("Вечер")
else:
    print("Ночь")

password = "qwerty123"
if len(password) < 6:
    print("Слишком короткий пароль")
elif password.isdigit():
    print("Пароль не должен состоять только из цифр")
elif password.islower() or password.isupper():
    print("Добавь разные регистры")
else:
    print("Пароль выглядит нормально")


