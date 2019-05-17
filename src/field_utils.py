from enum import Enum

class FieldRow(Enum):
    HEADER = 0
    NORTH = 1
    WEST_EAST = 2
    SOUTH = 3
    FOOTER = 4

class FieldSideType(Enum):
    STOP = 0
    ENTRANCE = 1
    EXIT = 2