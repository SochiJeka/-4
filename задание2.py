def process_input(data):
    while True:
        if isinstance(data, list):
            # Среднее геометрическое чисел в списке
            product = 1
            for num in data:
                product *= num
            geometric_mean = product ** (1 / len(data))
            return geometric_mean

        elif isinstance(data, dict):
            # Сортировка словаря по значениям в порядке убывания
            sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
            return sorted_dict

        elif isinstance(data, int):
            # Проверка, является ли число простым
            if data < 2:
                return False
            for i in range(2, int(data ** 0.5) + 1):
                if data % i == 0:
                    return False
            return True

        elif isinstance(data, str):
            # Подсчет количества слов в строке и поиск самого длинного слова
            words = data.split()
            word_count = len(words)
            longest_word = max(words, key=len)
            return word_count, longest_word

        else:
            print("Неверный тип данных. Попробуйте еще раз.")
            data = input("Введите данные: ")

data = input("Введите данные: ")
result = process_input(data)
print(f"Результат: {result}")