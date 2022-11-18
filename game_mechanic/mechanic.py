import time
from random import randint
from time import perf_counter, monotonic


class List15:

    def movement(self, list15: list, move_to: int) -> list:
        """
        receive direction and make a movement zero to this direction
        :param list15: current field
        :param move_to: direction of movement
            1 - zero to up
            2 - zero to down
            3 - zero to right
            4 - zero to left
        :return: list15 after zero migrate
        """
        # looking for zero's coordinate
        for row_zero in range(4):
            try:
                col_zero = list15[row_zero].index(0)
                break
            except Exception:
                col_zero = None

        # movement figure to zero position
        # zero to up
        if move_to == 1 and row_zero != 0:
            list15[row_zero][col_zero], list15[row_zero - 1][col_zero] = list15[row_zero - 1][col_zero], \
                                                                         list15[row_zero][col_zero]
            row_zero -= 1
        # zero to down
        elif move_to == 2 and row_zero != 3:
            list15[row_zero][col_zero], list15[row_zero + 1][col_zero] = list15[row_zero + 1][col_zero], \
                                                                         list15[row_zero][col_zero]
            row_zero += 1
        # zero to right
        elif move_to == 3 and col_zero != 3:
            list15[row_zero][col_zero], list15[row_zero][col_zero + 1] = list15[row_zero][col_zero + 1], \
                                                                         list15[row_zero][col_zero]
            col_zero += 1
        # zero to left
        elif move_to == 4 and col_zero != 0:
            list15[row_zero][col_zero], list15[row_zero][col_zero - 1] = list15[row_zero][col_zero - 1], \
                                                                         list15[row_zero][col_zero]
            col_zero -= 1
        return list15

    def new_list(self) -> list:
        """
        create new list 15
        :return: list15 in right order
        """
        list15 = [[i + 4 * j for i in range(4)] for j in range(4)]
        return list15

    def mixer(self) -> list:
        """
        mixes list15 to start game
            1 - zero to up
            2 - zero to down
            3 - zero to right
            4 - zero to left
        :return: movement direction
        """
        list15 = self.new_list()
        # choose random direction to move zero
        for _ in range(1):
            move_to = randint(1, 5)
            self.movement(list15, 2)
        return list15


class Timer:
    def __init__(self):
        self.start_time = None
        self.counter_time = None

    def start_timer(self):
        if self.start_time is not None:
            print('Timer works')
        self.start_time = perf_counter()

    def diff_timer(self):
        self.counter_time = perf_counter() - self.start_time
        print(f'Timer: {self.counter_time}')

    def __enter__(self):
        self.start_timer()

    def __exit__(self, *kwargs):
        self.diff_timer()


def the_game():
    print("Let's start:")
    mixed_field = List15().mixer()
    print(*mixed_field, sep='\n')
    sample = List15().new_list()
    counter = 0

    with Timer():
        while sample != mixed_field:
            print(f"Movements: {counter}")
            move_to = int(
                input('Choose zero to move: 1 - zero to up, 2 - zero to down, 3 - zero to right, 4 - zero to left: '))
            mixed_field = List15().movement(mixed_field, move_to)
            print(*mixed_field, sep='\n')
            counter += 1

        return print(f"Congratulations! You've done it after {counter} movements!")
