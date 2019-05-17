from field import Field, FieldRow

class Board:
    SIZE = 3

    __fields = []

    def __init__(self):
        for row in range(Board.SIZE):
            row_array = []
            for column in range(Board.SIZE):
                field = Field()
                if row == 0 and column == 0:
                    field.is_start_field()
                elif row == Board.SIZE-1 and column == Board.SIZE-1:
                    field.is_end_field()
                row_array.append(field)
            self.__fields.append(row_array)

    def draw(self):
        for row in self.__fields:
            for field_row in range(5):
                for field in row:
                    field.draw(FieldRow(field_row))
                    print('  ', end='')
                print()
