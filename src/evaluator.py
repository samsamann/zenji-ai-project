import copy
from field_utils import FieldSideTypes
from operator import itemgetter

class RotationTracker:

    def __init__(self, field):
        self.__field = field
        self.__rotation = 0
        self.__entrance_side = -1
        self.__exit_side = -1

    def get_field(self):
        return self.__field
    
    def get_rotation_count(self):
        return self.__rotation

    def set_side_type(self, side_type, pos):
        if side_type == FieldSideTypes.ENTRANCE:
            self.__entrance_side = pos
        elif side_type == FieldSideTypes.EXIT:
            self.__exit_side = pos
    
    def get_side_type(self):
        return (self.__entrance_side, self.__exit_side)
    
    def inc(self):
        self.__rotation += 1


class Evaluator:

    def __init__(self):
        self.__possible_paths = []

    def evaluate(self, board):
        self.__board = copy.deepcopy(board)
        start_field = self.__board.get_start_field()
        rotation_tracker = RotationTracker(start_field)
        for i in range(4):
            self.__deep_search(start_field, [], [rotation_tracker], -1)
            start_field.rotate_clockwise()
            rotation_tracker.inc()

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
            

    def __deep_search(self, field, visited_fields, rotation_hist, connected_side):
        if not field.is_start_field():
            rotation_hist[-2].set_side_type(FieldSideTypes.EXIT, connected_side)
        
        if field.is_end_field():
            return True

        visited_fields.append(field)
        
        for neighbor_field in self.__board.get_neighbor_fields(field):
            rotation_tracker = RotationTracker(neighbor_field)
            # rotate 4 times to return to initial position
            for i in range(4):
                if neighbor_field not in visited_fields:
                    side_type = self.__board.get_neighbor_side_type(field, neighbor_field)
                    if side_type == FieldSideTypes.ENTRANCE:
                        connected_sides = self.__board.get_connected_sides(field, neighbor_field)
                        rotation_tracker.set_side_type(FieldSideTypes.ENTRANCE, connected_sides[1])
                        rotation_hist.append(rotation_tracker)
                        if self.__deep_search(neighbor_field, visited_fields, rotation_hist, connected_sides[0]):
                            self.__possible_paths.append(copy.deepcopy(rotation_hist))
                        rotation_hist.remove(rotation_tracker)
                neighbor_field.rotate_clockwise()
                rotation_tracker.inc()

        visited_fields.remove(field)
        return False
