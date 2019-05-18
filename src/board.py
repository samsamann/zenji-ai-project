from field import Field
from renderer import BoardRender

class Board:
    __renderer = BoardRender()

    def __init__(self, board_config):
        self.__fields = []
        row_count = len(board_config)
        for row_id, row in enumerate(board_config):
            column_count = len(row)
            # we need a square board
            assert column_count == row_count, 'Check board configuration'
            row_array = []
            for column_id, field_config in enumerate(row):
                assert len(field_config) == 4, 'Field configuration must contain 4 side types'
                field = Field(
                    field_config,
                    row_id == 0 and column_id == 0,
                    row_id == row_count - 1 and column_id == column_count - 1
                )
                row_array.append(field)
            self.__fields.append(row_array)

    def get_fields(self):
        return self.__fields

    def draw(self, board = None):
        if board is None:
            self.__renderer.draw(self.get_fields())
        else:
            self.__renderer.draw(self.get_fields(), board.get_fields())
