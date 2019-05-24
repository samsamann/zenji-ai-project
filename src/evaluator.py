import copy
from field_utils import FieldSideTypes
from operator import itemgetter

class RotationTracker:

    def __init__(self, field):
        self.__field = field
        self.__rotation = 0

    def get_field(self):
        return self.__field
    
    def get_rotation_count(self):
        return self.__rotation
    
    def inc(self):
        self.__rotation += 1


class Evaluator:

    def __init__(self):
        self.__possible_paths = []

    def evaluate(self, board):
        self.__board = copy.deepcopy(board)
        # self.__deep_search(self.__board.get_start_field())
        start_field = self.__board.get_start_field()
        rotation_tracker = RotationTracker(start_field)
        for i in range(4):
            if len(self.__board.get_neighbor_fields(start_field)) > 0:
                self.__deep_search(start_field, [start_field], [rotation_tracker])
            start_field.rotate_clockwise()
            rotation_tracker.inc()
        return self.__board

    def count_possible_paths(self):
        return len(self.__possible_paths)

    def get_fastest_path(self):
        paths = []
        for path in self.__possible_paths:
            total_rotation = 0
            total_fields = 0
            for tracker in path:
                total_rotation += tracker.get_rotation_count()
                total_fields += 1
            paths.append((total_rotation, total_fields, path))
        paths = sorted(paths, key=itemgetter(0,1))
        return paths[0]
            

    def __deep_search(self, field, visited_fields, rotation_hist):
        if field.is_end_field():
            return True

        visited_fields.append(field)
        
        for neighbor_field in self.__board.get_neighbor_fields(field):
            rotation_tracker = RotationTracker(neighbor_field)
            # rotate 4 times to return to initial position
            for i in range(4):
                if neighbor_field not in visited_fields:
                    if self.__board.get_neighbor_side_type(field, neighbor_field) == FieldSideTypes.ENTRANCE:
                        rotation_hist.append(rotation_tracker)
                        if self.__deep_search(neighbor_field, visited_fields, rotation_hist):
                            self.__possible_paths.append(copy.deepcopy(rotation_hist))
                        rotation_hist.remove(rotation_tracker)
                neighbor_field.rotate_clockwise()
                rotation_tracker.inc()

        visited_fields.remove(field)
        return False
