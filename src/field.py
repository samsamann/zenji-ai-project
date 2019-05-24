from field_utils import FieldRows, FieldSideTypes
from renderer import FieldRenderer

#
# [0, 1, 2, 0]
#
class Field:
    __renderer = FieldRenderer()

    def __init__(self, field_config, pos, board_size = (0, 0)):
        self.__pos = pos
        self.__board_size = board_size
        self.__side_types = []
        for idx, side_type in enumerate(field_config):
            if idx >= 0 and idx < 4:
                self.__side_types.insert(idx, FieldSideTypes(side_type))

    def get_pos(self):
        return self.__pos

    def is_start_field(self):
        return self.__pos[0] == 0 and self.__pos[1] == 0

    def is_end_field(self):
        return self.__pos[0] == self.__board_size[0]-1 and self.__pos[1] == self.__board_size[1]-1

    def get_north_type(self):
        return self.__side_types[0]

    def get_east_type(self):
        return self.__side_types[1]

    def get_south_type(self):
        return self.__side_types[2]

    def get_west_type(self):
        return self.__side_types[3]

    def draw(self, row, rotate_tracker = None):
        self.__renderer.draw(self, FieldRows(row), rotate_tracker)

    def rotate_clockwise(self):
        old_west_type = self.__side_types[3]
        del self.__side_types[3]
        self.__side_types.insert(0, old_west_type)

    def __eq__(self, other):
        self_pos = self.get_pos()
        other_pos = other.get_pos()
        return self_pos[0] == other_pos[0] and self_pos[1] == other_pos[1]
