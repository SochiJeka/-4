def is_password_good(password):
    # Проверка длины пароля
    if len(password) < 8:
        return False

    # Проверка наличия заглавной буквы
    if not any(char.isupper() for char in password):
        return False

    # Проверка наличия цифры
    if not any(char.isdigit() for char in password):
        return False

    # Если все проверки пройдены, пароль считается надежным
    return True

while True:
    # Получение пароля от пользователя
    password = input("Введите пароль: ")

    # Проверка надежности пароля
    result = is_password_good(password)

    # Если пароль надежный, выходим из цикла
    if result:
        break

    print("Пароль ненадежный. Попробуйте еще раз.")

print("Пароль надежный")