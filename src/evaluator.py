import copy
from field_utils import FieldSideTypes

class Evaluator:

    def __init__(self):
        self.__possible_paths = []

    def evaluate(self, board):
        self.__board = copy.deepcopy(board)
        self.__deep_search(self.__board.get_start_field())

        return self.__board

    def get_possible_paths(self):
        return self.__possible_paths

    def __deep_search(self, field, rotation_count = 0, visited_fields = []):
        visited_fields.append(field)
        
        if field.is_end_field():
            return True
        
        for neighbor_field in self.__board.get_neighbor_fields(field):
            if neighbor_field not in visited_fields:
                for i in range(4):
                    if self.__board.get_neighbor_side_type(field, neighbor_field) == FieldSideTypes.ENTRANCE:
                        if self.__deep_search(neighbor_field, rotation_count + i, visited_fields):
                            self.__possible_paths.append((visited_fields, rotation_count))
                    neighbor_field.rotate_clockwise()
        return False
