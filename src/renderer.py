from field_utils import FieldSideTypes

class FieldRenderer:

    __TRIANGLE_UP = '▲'
    __TRIANGLE_DOWN = '▼'

    __TRIANGLE_LEFT = '◀'
    __TRIANGLE_RIGHT = '▶'

    __START_POINT = '✺'
    __END_POINT = '='

    __CENTER_SYMBOL = '+'
    __DEFAULT_SYMBOL = 'x'

    def draw(self, field, row):
        method_name = '_FieldRenderer__draw_' + str(row.name).lower()
        method = getattr(self, method_name, lambda field: print('wrong name'))
        method(field)
    
    def __draw_header(self, field):
        print('_' * 9, end='')

    def __draw_north(self, field):
        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_north_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_DOWN
        elif field.get_north_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_UP
        print('|' + ' ' * 3 + field_symbol + ' ' * 3 + '|', end='')

    def __draw_west_east(self, field):
        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_west_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_RIGHT
        elif field.get_north_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_LEFT
        print('| ' + field_symbol, end='')

        center_symbol = self.__CENTER_SYMBOL
        if field.is_start_field():
            center_symbol = self.__START_POINT
        elif field.is_end_field():
            center_symbol = self.__END_POINT
        print(' ' + center_symbol + ' ', end='')

        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_east_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_LEFT
        elif field.get_east_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_RIGHT
        print(field_symbol + ' |', end='')

    def __draw_south(self, field):
        field_symbol = self.__DEFAULT_SYMBOL
        if field.get_south_type() == FieldSideTypes.ENTRANCE:
            field_symbol = self.__TRIANGLE_UP
        elif field.get_south_type() == FieldSideTypes.EXIT:
            field_symbol = self.__TRIANGLE_DOWN
        print('|' + ' ' * 3 + field_symbol + ' ' * 3 + '|', end='')

    def __draw_footer(self, field):
        print('‾' * 9, end='')



class BoardRender:

    def draw(self, fields):
        for row in fields:
            for field_row in range(5):
                for field in row:
                    field.draw(field_row)
                    print('  ', end='')
                print()
