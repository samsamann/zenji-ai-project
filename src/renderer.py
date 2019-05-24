import copy
from field_utils import FieldSideTypes, FieldColors

class FieldRenderer:

    __TRIANGLE_UP = '▲'
    __TRIANGLE_DOWN = '▼'

    __TRIANGLE_LEFT = '◀'
    __TRIANGLE_RIGHT = '▶'

    __START_POINT = '✺'
    __END_POINT = '='

    __CENTER_SYMBOL = '+'
    __DEFAULT_SYMBOL = 'x'

    def draw(self, field, row, rotate_tracker = None):
        method_name = '_FieldRenderer__draw_' + str(row.name).lower()
        method = getattr(self, method_name, lambda field, rotate_tracker: print('wrong name'))
        method(field, rotate_tracker)
    
    def __draw_header(self, field, rotate_tracker):
        print('_' * 9, end='')

    def __draw_north(self, field, rotate_tracker):
        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_north_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_DOWN
        elif field.get_north_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_UP
        field_symbol = self.__colorize_sides(field_symbol, rotate_tracker, 0)
        print('|' + ' ' * 3 + field_symbol + ' ' * 3 + '|', end='')

    def __draw_west_east(self, field, rotate_tracker):
        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_west_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_RIGHT
        elif field.get_west_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_LEFT
        print('| ' + self.__colorize_sides(field_symbol, rotate_tracker, 3), end='')

        center_symbol = self.__CENTER_SYMBOL
        if field.is_start_field():
            center_symbol = FieldColors.RED + self.__START_POINT + FieldColors.CLEAR
        elif field.is_end_field():
            center_symbol = FieldColors.RED + self.__END_POINT + FieldColors.CLEAR
        elif rotate_tracker is not None:
            center_symbol = FieldColors.BLUE + center_symbol + FieldColors.CLEAR
        print(' ' + center_symbol + ' ', end='')

        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_east_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_LEFT
        elif field.get_east_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_RIGHT
        field_symbol = self.__colorize_sides(field_symbol, rotate_tracker, 1)
        print(field_symbol + ' |', end='')

    def __draw_south(self, field, rotate_tracker):
        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_south_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_UP
        elif field.get_south_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_DOWN
        field_symbol = self.__colorize_sides(field_symbol, rotate_tracker, 2)
        print('|' + ' ' * 3 + field_symbol + ' ' * 3 + '|', end='')

    def __draw_footer(self, field, rotate_tracker):
        print('‾' * 9, end='')

    def __colorize_sides(self, field_symbol, rotate_tracker, side):
        if rotate_tracker is not None:
            side_types = rotate_tracker.get_side_type()
            if side_types[0] == side or side_types[1] == side:
                return FieldColors.BLUE + field_symbol + FieldColors.CLEAR
        return field_symbol



class BoardRender:

    def draw(self, fields, path = []):
        if len(path) == 0:
            self.__draw_one_board(fields)
        else:
            self.__draw_two_boards(fields, path)

    def __draw_one_board(self, fields):
        for row in fields:
            for field_row in range(5):
                for field in row:
                    field.draw(field_row)
                    print('  ', end='')
                print()

    def __draw_two_boards(self, fields, path):
        board2_fields = self.__rotate_fields(fields, path)
        print('INIT:' + ' ' * (9 * 5 + 3) + 'END:')
        for idx, row_board1 in enumerate(fields):
            row_board2 = board2_fields[idx]
            for field_row in range(5):
                for field in row_board1:
                    field.draw(field_row)
                    print('  ', end='')
                print(' ' * 9, end='')
                for field in row_board2:
                    rotate_trackers = self.__filter_rotate_trackers(path, field)
                    if len(rotate_trackers) > 0:
                        field.draw(field_row, rotate_trackers[0])
                    else:
                        field.draw(field_row)
                    print('  ', end='')
                print()

    def __rotate_fields(self, fields, path):
        copy_fields = copy.deepcopy(fields)
        for row in copy_fields:
            for field in row:
                rotate_trackers = self.__filter_rotate_trackers(path, field)
                if len(rotate_trackers) > 0:
                    for x in range(rotate_trackers[0].get_rotation_count()):
                        field.rotate_clockwise()
        return copy_fields

    def __filter_rotate_trackers(self, path, field):
        return list(
            filter(
                lambda path_item: path_item if path_item.get_field() == field else None,
                path
            )
        )
