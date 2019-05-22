from field import Field
from field_utils import FieldSideTypes
from renderer import BoardRender

class Board:
    __renderer = BoardRender()

    def __init__(self, board_config):
        self.__fields = []
        row_count = len(board_config)
        self.__size = (row_count, row_count)
        for row_id, row in enumerate(board_config):
            column_count = len(row)
            # we need a square board
            assert column_count == row_count, 'Check board configuration'
            row_array = []
            for column_id, field_config in enumerate(row):
                assert len(field_config) == 4, 'Field configuration must contain 4 side types'
                field = Field(field_config, (column_id, row_id), (column_count, row_count))
                row_array.append(field)
            self.__fields.append(row_array)
    
    def get_start_field(self):
        return self.__fields[0][0]

    def get_neighbor_fields(self, field):
        neighbors = []
        pos = field.get_pos()
        if pos[1] > 0 and field.get_north_type() == FieldSideTypes.EXIT:
            neighbors.append(self.__fields[pos[1] - 1][pos[0]])
        if pos[0] < self.__size[0] - 1 and field.get_east_type() == FieldSideTypes.EXIT:
            neighbors.append(self.__fields[pos[1]][pos[0] + 1])
        if pos[1] < self.__size[1] - 1 and field.get_south_type() == FieldSideTypes.EXIT:
            neighbors.append(self.__fields[pos[1] + 1][pos[0]])
        if pos[0] > 0 and field.get_west_type() == FieldSideTypes.EXIT:
            neighbors.append(self.__fields[pos[1]][pos[0] - 1])
        return neighbors

    def get_fields(self):
        return self.__fields

    def draw(self, board = None):
        if board is None:
            self.__renderer.draw(self.get_fields())
        else:
            self.__renderer.draw(self.get_fields(), board.get_fields())

    def get_neighbor_side_type(self, origin, dest):
        origin_pos = origin.get_pos()
        dest_pos = dest.get_pos()
        if origin_pos[0] == dest_pos[0] and origin_pos[1] == dest_pos[1]:
            raise Exception('Field one and field two are not vertical or horizontal neighbors')
        
        if origin_pos[0] == dest_pos[0] and origin_pos[1] > dest_pos[1]:
            return dest.get_south_type()
        if origin_pos[1] == dest_pos[1] and origin_pos[0] < dest_pos[0]:
            return dest.get_west_type()
        if origin_pos[0] == dest_pos[0] and origin_pos[1] < dest_pos[1]:
            return dest.get_north_type()
        if origin_pos[1] == dest_pos[1]  and origin_pos[0] > dest_pos[0]:
            return dest.get_east_type()
