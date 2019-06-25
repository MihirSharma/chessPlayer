import numpy as np

class board:
    board = np.ndarray([8,8], dtype = "uint8")

class pawn(object):
    def __init__(self, position, team):
        self.piece_type = "pawn"
        self.current_position_self = position
        self.team = team
        print(self.current_position_self)
        print(self.team)
        print(self.piece_type)
    move_ctr_self = 0
    def move(self, x):
        if self.move_ctr_self == 0:
            permitied_move = [self.current_position_self[1] + 2, self.current_position_self[1] + 1]
        else:
            permitied_move = [self.current_position_self[1] + 2, self.current_position_self[1] + 1]

class rook:
    def __init__(self, position, team):
        self.current_position_self = position
        self.team = team
        self.piece_type = "rook"
        print(self.current_position_self)
        print(self.team)
        print(self.piece_type)
    move_ctr_self = 0
    def move(self, x):
        permitied_move = [[self.current_position_self[1] + x], [self.current_position_self[1] - x],
        [self.current_position_self[0] + x], [self.current_position_self[0] - x]]

class knight:
    def __init__(self, position, team):
        self.current_position_self = position
        self.team = team
        self.piece_type = "knight"
        print(self.current_position_self)
        print(self.team)
        print(self.piece_type)
    move_ctr_self = 0
    def move(self):
        permitied_move = [[self.current_position_self[0] + 2, self.current_position_self[1] + 1], [self.current_position_self[0] + 1, self.current_position_self[1] + 2], 
        [self.current_position_self[0] - 1, self.current_position_self[1] - 2], [self.current_position_self[0] - 2, self.current_position_self[1] - 1], 
        [self.current_position_self[0] + 2, self.current_position_self[1] - 1], [self.current_position_self[0] + 1, self.current_position_self[1] - 2], 
        [self.current_position_self[0] - 2, self.current_position_self[1] + 1], [self.current_position_self[0] - 1, self.current_position_self[1] + 2]]

class bishop:
    def __init__(self, position, team):
        self.current_position_self = position
        self.team = team
        self.piece_type = "bishop"
        print(self.current_position_self)
        print(self.team)
        print(self.piece_type)
    move_ctr_self = 0
    def move(self, x):
        permitied_move = [[self.current_position_self[0] + x, self.current_position_self[1] + x], [self.current_position_self[0] - x, self.current_position_self[1] - x],
        [self.current_position_self[0] + x, self.current_position_self[1] - x], [self.current_position_self[0] - x, self.current_position_self[1] + x]]

class queen:
    def __init__(self, position, team):
        self.current_position_self = position
        self.team = team
        self.piece_type = "queen"
        print(self.current_position_self)
        print(self.team)
        print(self.piece_type)
    move_ctr_self = 0
    def move(self, x):
        permitied_move = [[self.current_position_self[0] + x, self.current_position_self[1] + x], [self.current_position_self[0] - x, self.current_position_self[1] - x],
        [self.current_position_self[0] + x, self.current_position_self[1] - x], [self.current_position_self[0] - x, self.current_position_self[1] + x],
        [self.current_position_self[1] + x], [self.current_position_self[1] - x],
        [self.current_position_self[0] + x], [self.current_position_self[0] - x]]

class king:
    def __init__(self, position, team):
        self.current_position_self = position
        self.team = team
        self.piece_type = "king"
        print(self.current_position_self)
        print(self.team)
        print(self.piece_type)
    move_ctr_self = 0
    def move(self, x):
        permitied_move = [[self.current_position_self[0] + 1, self.current_position_self[1] + 1], [self.current_position_self[0] - 1, self.current_position_self[1] - 1],
        [self.current_position_self[0] + 1, self.current_position_self[1] - 1], [self.current_position_self[0] - 1, self.current_position_self[1] + 1],
        [self.current_position_self[1] + 1], [self.current_position_self[1] - 1],
        [self.current_position_self[0] + 1], [self.current_position_self[0] - 1]]

def initialize_game():
    white_names_pawns = ['wp0', 'wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7']
    black_names_pawns = ['bp0', 'bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7']
    white_names_pieces = ['wr1', 'wk1', 'wb1', 'wq', 'wking', 'wb3', 'wk2', 'wr2']
    black_names_pieces = ['br1', 'bk1', 'bb1', 'bq', 'bking', 'bb3', 'bk2', 'br2']
    for i in range(0,8):
        vars()[white_names_pawns[i]] = pawn(position = [i, 1], team = "white")
    print("\n")
    for i in range(0,8):
        vars()[black_names_pawns[i]] = pawn(position = [i, 6], team = "black")
    print("\n")
    
    wr1 = rook(position = [0,0], team = "white")
    wr2 = rook(position = [7,0], team = "white")
    wk1 = knight(position = [1,0], team = "white")
    wk2 = knight(position = [6,0], team = "white")
    wb1 = bishop(position = [2,0], team = "white")
    wb2 = bishop(position = [5,0], team = "white")
    wq = queen(position = [3,0], team = "white")
    wking = king(position = [4,0], team = "white")
    
    print("\n")

    br1 = rook(position = [0,7], team = "black")
    br2 = rook(position = [7,7], team = "black")
    bk1 = knight(position = [1,7], team = "black")
    bk2 = knight(position = [6,7], team = "black")
    bb1 = bishop(position = [2,7], team = "black")
    bb2 = bishop(position = [5,7], team = "black")
    bq = queen(position = [3,7], team = "black")
    bking = king(position = [4,7], team = "black")
    
    

initialize_game()