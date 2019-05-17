from enum import Enum

class FieldRow(Enum):
    HEADER = 0
    NORTH = 1
    WEST_EAST = 2
    SOUTH = 3
    FOOTER = 4

class Field:
    __is_start = False
    __is_end = False

    __NORTH_ENTRANCE = '▼'
    __NORTH_EXIT = '▲'

    __SOUTH_ENTRANCE = '▲'
    __SOUTH_EXIT = '▼'

    __EAST_ENTRANCE = '◀'
    __EAST_EXIT = '▶'

    __WEST_ENTRANCE = '▶'
    __WEST_EXIT = '◀'

    __START_POINT = '✺'
    __END_POINT = '='

    def is_start_field(self):
        self.__is_start = True
        self.__is_end = False

    def is_end_field(self):
        self.__is_start = False
        self.__is_end = True

    def draw(self, row = FieldRow(0)):
        method_name = '_Field__draw_' + str(row.name).lower()
        method = getattr(self, method_name, lambda: print('wrong'))
        method()
        
    def __draw_header(self):
        print('_' * 9, end='')

    def __draw_north(self):
        print('|' + ' ' * 3, end='')
        print(self.__NORTH_ENTRANCE, end='')
        print(' ' * 3 + '|', end='')

    def __draw_west_east(self):
        print('| ', end='')
        print(self.__EAST_ENTRANCE, end='')
        print(' + ', end='')
        print(self.__WEST_EXIT, end='')
        print(' |', end='')

    def __draw_south(self):
        print('|' + ' ' * 3, end='')
        print(self.__NORTH_ENTRANCE, end='')
        print(' ' * 3 + '|', end='')

    def __draw_footer(self):
        print('‾' * 9, end='')
