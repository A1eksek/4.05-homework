первая задача
def NOD(a, b):
    if b == 0:
        return a
    else:
        return NOD(b, a % b)

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
result = NOD(a, b)
print(f'Наибольший общий делитель {a} и {b} равен {result}.')
Вторая задача


import random


def try_it(secret_number, attempts):
    guess = input("Введите 4-х значное число (цифры должны быть уникальными): ")

    # Проверяем корректность ввода
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) < 4:
        print("Ошибка: введите 4 уникальные цифры.")
        return try_it(secret_number, attempts)

    beefs = 0  # кол-во цифр на неправильных местах
    cows = 0  # кол-во цифр на правильных местах

    # Подсчет быков и коров
    for i in range(4):
        digit = int(guess[i])
        if secret_number[i] == digit:
            cows += 1
            beefs += 1  #
        elif digit in secret_number:
            beefs += 1

    print(f"\nБыки = {beefs}\tКоровы = {cows}")

    # Проверка на успех
    if cows == 4:
        print(f"Вы угадали! Потрачено {attempts} попыток!")
    else:
        return try_it(secret_number, attempts + 1)


def main():
    random.seed()
    secret_number = random.sample(range(10), 4)
    print("Компьютер загадал четырёхзначное число.\n")
    try_it(secret_number, 1)

if __name__ == "__main__":
    main()
4 задача
import random


def initialize_board():
    board = list(range(1, 16)) + [None]
    random.shuffle(board)
    return [board[i:i + 4] for i in range(0, 16, 4)]


def print_board(board):
    for row in board:
        print(" | ".join(str(x).rjust(2, ' ') if x is not None else '  ' for x in row))
        print("-" * 21)


def find_empty_space(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] is None:
                return i, j


def is_winnable(board):
    flatten_board = [num for row in board for num in row if num is not None]
    inversions = sum(1 for i in range(len(flatten_board)) for j in range(i + 1, len(flatten_board)) if
                     flatten_board[i] > flatten_board[j])
    return (inversions % 2) == 0


def can_move(empty_x, empty_y, target_x, target_y):
    return (empty_x == target_x and abs(empty_y - target_y) == 1) or (
                empty_y == target_y and abs(empty_x - target_x) == 1)


def move_tile(board, tile_x, tile_y):
    empty_x, empty_y = find_empty_space(board)
    if can_move(empty_x, empty_y, tile_x, tile_y):
        board[empty_x][empty_y], board[tile_x][tile_y] = board[tile_x][tile_y], board[empty_x][empty_y]


def is_solved(board):
    return all(board[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4) if board[i][j] is not None)


def main():
    board = initialize_board()

    while not is_winnable(board):
        board = initialize_board()

    print("Добро пожаловать в игру 'Пятнашки'!")
    print_board(board)

    while not is_solved(board):
        try:
            move = input("Введите номер плитки для перемещения (или 'exit' для выхода): ")
            if move == 'exit':
                break
            move = int(move)

            # Найти координаты плитки
            tile_x, tile_y = next(((i, j) for i in range(4) for j in range(4) if board[i][j] == move), (None, None))
            if tile_x is not None and tile_y is not None:
                move_tile(board, tile_x, tile_y)
                print_board(board)
            else:
                print("Плитка не найдена на доске.")
        except ValueError:
            print("Пожалуйста, введите корректный номер плитки.")

    if is_solved(board):
        print("Поздравляем! Вы выиграли!")
    else:
        print("Выход из игры.")


if __name__ == "__main__":
    main()
