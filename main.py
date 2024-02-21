from typing import Tuple, List
from os import name, system
from random import randint, choice


'''

 FIELD

   0 1 2
A0  | | |
B1  | | |
C2  | | |


'''


WINNING_COMBINATIONS = [((0, 0), (1, 0), (2, 0)),
                        ((0, 1), (1, 1), (2, 1)),
                        ((0, 2), (1, 2), (2, 2)),
                        ((0, 0), (0, 1), (0, 2)),
                        ((1, 0), (1, 1), (1, 2)),
                        ((2, 0), (2, 1), (2, 2)),
                        ((0, 0), (1, 1), (2, 2)),
                        ((0, 2), (1, 1), (2, 0))]


def clear_screen() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

class Player:
    def __init__(self,
                 image: str,
                 is_auto=True,
                 ) -> None:
        self.is_auto = is_auto
        self.image = image

    def make_turn(self, field:list) -> None:
        if self.is_auto:
            counter = 0
            while True:
                counter += 1
                y = randint(0, 2)
                x = randint(0, 2)
                if field[y][x] == ' ':
                    field[y][x] = self.image
                    break
                if counter >= 20:
                    break



class Game:
    def __init__(self) -> None:
        self.field = [[' ' for i in range(3)] for i in range(3)]
        self.player_1 = Player(image='X')
        self.player_2 = Player(image='O')
        self.turns = 0
        self.is_running = 1
        self.main_loop()
    
    def check_winner(self) -> None:
        for i, j, k in WINNING_COMBINATIONS:
            if self.field[i[0]][i[1]] == 'X':
                if self.field[j[0]][j[1]] == 'X':
                    if self.field[k[0]][k[1]] == 'X':
                        self.field[i[0]][i[1]] = u'\033[9m' + self.field[i[0]][i[1]] + u'\033[0m'
                        self.field[j[0]][j[1]] = u'\033[9m' + self.field[j[0]][j[1]] + u'\033[0m'
                        self.field[k[0]][k[1]] = u'\033[9m' + self.field[k[0]][k[1]] + u'\033[0m'
                        self.is_running = 0
                        self.print_field()
                        print('Игрок победил')
                        input()
                        return self.main_loop()

            elif self.field[i[0]][i[1]] == 'O':
                if self.field[j[0]][j[1]] == 'O':
                    if self.field[k[0]][k[1]] == 'O':
                        self.field[i[0]][i[1]] = u'\033[9m' + self.field[i[0]][i[1]] + u'\033[0m'
                        self.field[j[0]][j[1]] = u'\033[9m' + self.field[j[0]][j[1]] + u'\033[0m'
                        self.field[k[0]][k[1]] = u'\033[9m' + self.field[k[0]][k[1]] + u'\033[0m'
                        self.is_running = 0
                        self.print_field()
                        print('Машина победила')
                        input()
                        return self.main_loop()

    def main_loop(self) -> None:
        while self.is_running:
            if self.turns < 9:
                self.print_field()
                self.player_1.make_turn(self.field)
                self.player_2.make_turn(self.field)
                self.turns += 2
                self.check_winner()

            if self.turns >= 9:
                self.print_field()
                print('Ничья!')
                self.is_running = 0
                break

    def print_field(self) -> None:
        clear_screen()
        print('   1 2 3')
        for index_y, row in enumerate(self.field):
            print(f' {index_y + 1}', end='')

            print('│', end='')
            for index_x, _ in enumerate(row):
                print(self.field[index_y][index_x], end='')
                print('│', end='')
            print('')

    def get_user_input(self) -> Tuple[int]:
        turn = input('Введите координаты хода в формате 1 2: ')
        y, x = tuple(map(int, turn.split()))
        if y <= 3 and x <= 3:
            return y, x
        else:
            clear_screen()
            print('Координата должна быть не больше трех')
            print('')
            input('Нажмите ENTER чтобы продолжить')
            return self.main_loop()

    def get_empty_cells(self) -> List[tuple]:
        empty = []
        for index_y, row in enumerate(self.field):
            for index_x, _ in enumerate(row):
                if not self.field[index_y][index_x] == ' ':
                    empty.append((index_y, index_x))
        return empty


Game()
