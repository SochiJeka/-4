def create_chessboard(n, m):
    chessboard = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append("%")
            else:
                row.append("&")
        chessboard.append(row)
    chessboard[0][0] = "."
    return chessboard

n = input("Введите количество строк (n): ")
m = input("Введите количество столбцов (m): ")

# Проверка ввода количества строк
while not n.isdigit() or int(n) <= 0:
    print("Неверный ввод. Введите положительное целое число для количества строк.")
    n = input("Введите количество строк (n): ")

# Проверка ввода количества столбцов
while not m.isdigit() or int(m) <= 0:
    print("Неверный ввод. Введите положительное целое число для количества столбцов.")
    m = input("Введите количество столбцов (m): ")

n = int(n)
m = int(m)

board = create_chessboard(n, m)

# Вывод двумерного массива
for row in board:
    print(" ".join(row))