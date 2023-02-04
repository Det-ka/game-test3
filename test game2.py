def greet():    # Привецевие
    print("___________________")
    print("  Привецтвуем вас  ")
    print("      в игре       ")
    print("  крестики нолики  ")
    print("___________________")
    print("    формат ввода   ")
    print(" x - номер строки  ")
    print(" y - номер толбца  ")

def show():     #Вывод карты на экран
    print()
    print("    | 0 | 1 | 2 | ")
    print("------------------")
    for i, row in enumerate(maps):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ----------------")
    print()

def ask():   # Сделать ход
    while True:
        cord = input(" Ваш ход : ").split()

        if len(cord) != 2:
            print(" Введите 2 координаты : ")
            continue

        x, y = cord

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите чсло :")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print(" Координаты вне диапазона !!! ")
            continue

        if maps[x][y] != " ":
            print(" Клетка занята !!!" )
            continue

        return x, y

def check_win():      #Выиграшные ломбинации
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(maps[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print(" Выиграл x ! ")
            return True
        if symbols ==["0", "0", "0"]:
            print(" Выиграл 0 ! ")
            return True
    return False

greet()      #конец
maps = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик ! ")
    else:
        print(" Ходит ноли ! ")

    x, y = ask()

    if count % 2 == 1:
        maps[x][y] = "x"
    else:
        maps[x][y] = "0"

    if check_win():
        break

    if count == 9:
        break