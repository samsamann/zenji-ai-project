from board import Board

board_config = [ \
    [[0, 2, 0, 0], [0, 0, 2, 1], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [1, 0, 2, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [1, 2, 0, 0], [0, 0, 0, 1]],
]

board = Board(board_config)
# draw init state
board.draw()
