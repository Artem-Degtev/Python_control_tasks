def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

field = [[" "] * 3 for i in range(3)]

def show():
    print()
    print(f'  | 0 | 1 | 2 |')
    print("-" * 15)
    print(f'0 | {field[0][0]} | {field[0][1]} | {field[0][2]} |')
    print("-"*15)
    print(f'1 | {field[1][0]} | {field[1][1]} | {field[1][2]} |')
    print("-" * 15)
    print(f'2 | {field[2][0]} | {field[2][1]} | {field[2][2]} |')
    print("-" * 15)

def ask():
    coordinat =  map(int, input('Ваш ход: ').split())

    x, y = coordinat
    if 0 <= x <= 2 and 0 <= y <= 2:
        if field[x][y] == " ":
            return x,y
        else:
            print(' Клетка занята! ')
    if not(x.isdigit()) or not (y.isdigit()):
        print('Введите число ')

    else:
        print(' Вне диапазона ')

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coordinat in win_cord:
        symbols = []
        for c in coordinat:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print('Ходит крестик ')
    else:
        print('Ходит нолик ')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'x'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print('Ничья ')
        break
