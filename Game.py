table = [1, 2, 3, 4, 5, 6, 7, 8, 9]

wins_cord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def table_game():
    print("-------------")
    for i in range(3):
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")
        print('-------------')


def point_input(player_point):
    while True:
        value = input("Выберите поле для: " + player_point + "?")
        if not (value in "123456789"):
            print("Неверное поле, повторите ввод: ")
            continue
        value = int(value)
        if str(table[value - 1]) in "XO":
            print("Клетка занята.")
            continue
        table[value - 1] = player_point
        break


def game_win():
    for each in wins_cord:
        if (table[each[0] - 1]) == (table[each[1] - 1]) == (table[each[2] - 1]):
            return table[each[1]]
    else:
        return False


def main():
    counter = 0
    while True:
        table_game()
        if counter % 2 == 0:
            point_input("X")
        else:
            point_input("O")
        if counter > 3:
            winner = game_win()
            if winner:
                table_game()
                print(winner, "выиграл")
                break
        counter += 1
        if counter > 8:
            table_game()
            print("Ничья!")
            break


main()
