# Карта игры
map = [0, 1, 2,
       3, 4, 5,
       6, 7, 8]


# Победные линии в игре
win_lines = [[0, 1, 2],
             [0, 3, 6],
             [0, 4, 8],
             [1, 4, 7],
             [2, 4, 6],
             [2, 5, 8],
             [3, 4, 5],
             [6, 7, 8]]

# Вывод карты на экран
def print_map():
    print(map[0], end='')
    print(map[1], end='')
    print(map[2])

    print(map[3], end='')
    print(map[4], end='')
    print(map[5])

    print(map[6], end='')
    print(map[7], end='')
    print(map[8])


# Ход игрока в ячейку
def step_map(step,symbol):
    try:
        ind = map.index(step)
        map[ind] = symbol
    except(ValueError):
        print(*"Эта клетка уже занята")


# Текущий результат игры
def get_result():
    win = ""

    for i in win_lines:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = "O"

    return win


# Основной код игры
game_over = False
player1 = True

while game_over == False:

    print_map()

    if player1 == True:
        symbol = "X"
        step = int(input("ИГРОК 1, ваш ход: "))

    else:
        symbol = "O"
        step = int(input("ИГРОК 2, ваш ход: "))

    step_map(step, symbol)
    win = get_result()
    if win != "":
        game_over = True

    else:
        game_over = False

    # else:
    #     print("Ничья")
    #     game_over = True
    #     break

    player1 = not(player1)

# Конец игры
print_map()
print("Победил", win)