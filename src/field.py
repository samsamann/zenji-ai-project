from field_utils import FieldRow, FieldSideType
from renderer import FieldRenderer

#
# [0, 1, 2, 0]
#
class Field:
    __renderer = FieldRenderer()

    def __init__(self, field_config, is_start_field = False, is_end_field = False):
        self.__is_start = is_start_field
        self.__is_end = is_end_field
        for idx, side_type in enumerate(field_config):
            if idx == 0:
                self.__north = FieldSideType(side_type)
            elif idx == 1:
                self.__east = FieldSideType(side_type)
            elif idx == 2:
                self.__south = FieldSideType(side_type)
            elif idx == 3:
                self.__west = FieldSideType(side_type)

    def is_start_field(self):
        return self.__is_start

    def is_end_field(self):
        return self.__is_end

    def get_north_type(self):
        return self.__north

    def get_east_type(self):
        return self.__east

    def get_south_type(self):
        return self.__south

    def get_west_type(self):
        return self.__west

    def draw(self, row):
        self.__renderer.draw(self, FieldRow(row))
