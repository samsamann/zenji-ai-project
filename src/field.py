from field_utils import FieldRows, FieldSideTypes
from renderer import FieldRenderer

#
# [0, 1, 2, 0]
#
class Field:
    __renderer = FieldRenderer()

    def __init__(self, field_config, is_start_field = False, is_end_field = False):
        self.__is_start = is_start_field
        self.__is_end = is_end_field
        self.__side_types = []
        for idx, side_type in enumerate(field_config):
            if idx >= 0 and idx < 4:
                self.__side_types.insert(idx, FieldSideTypes(side_type))

    def is_start_field(self):
        return self.__is_start

    def is_end_field(self):
        return self.__is_end

    def get_north_type(self):
        return self.__side_types[0]

    def get_east_type(self):
        return self.__side_types[1]

    def get_south_type(self):
        return self.__side_types[2]

    def get_west_type(self):
        return self.__side_types[3]

    def draw(self, row):
        self.__renderer.draw(self, FieldRows(row))

    def rotate_clockwise(self):
        old_west_type = self.__side_types[3]
        del self.__side_types[3]
        self.__side_types.insert(0, old_west_type)
