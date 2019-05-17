from enum import Enum

class FieldRows(Enum):
    HEADER = 0
    NORTH = 1
    WEST_EAST = 2
    SOUTH = 3
    FOOTER = 4

class FieldSideTypes(Enum):
    STOP = 0
    ENTRANCE = 1
    EXIT = 2

class FieldColors:
    RED = '\033[91m'
    BLUE = '\033[94m'
    CLEAR = '\033[0m'
