def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except TypeError:
        print("Ошибка: неверный тип данных.")
    finally:
        print("Блок finally выполнен.")


# Запрос ввода числителя
while True:
    numerator = input("Введите числитель: ")
    try:
        numerator = int(numerator)
        break
    except ValueError:
        print("Ошибка: введите целое число.")

# Запрос ввода знаменателя
while True:
    denominator = input("Введите знаменатель: ")
    try:
        denominator = int(denominator)
        if denominator != 0:
            break
        else:
            print("Ошибка: знаменатель не может быть нулем.")
    except ValueError:
        print("Ошибка: введите целое число.")

# Вызов функции divide_numbers
result = divide_numbers(numerator, denominator)
print("Результат деления:", result)