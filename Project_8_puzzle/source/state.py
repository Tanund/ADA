class State:
    def __init__(self, goal_board, board, g_score, action=None, parent_state=None, h_method=None):
        self.board = board
        self.goal_board = goal_board
        self.size = len(board)
        self.parent_state = parent_state
        self.g_score = g_score
        self.action = action
        self.h_score = self.calculate_h(h_method)
        self.f_score = self.g_score + self.h_score

    def find_position_of_tile(self, board, value):
        # find the position of tile "value"
        for row in range(0, len(board)):
            for col in range(0, len(board)):
                if board[row][col] == value:
                    return (row, col)

    def calculate_h(self, h_method=None):
        h_score = 0
        if h_method == 'mht':
            # Manhattan method
            for row in range(0, self.size):
                for col in range(0, self.size):
                    value = self.board[row][col]
                    if value != 0:
                        # position of goal
                        (goal_row, goal_col) = self.find_position_of_tile(self.goal_board, value)
                        # position of init
                        (cur_row, cur_col) = self.find_position_of_tile(self.board, value)
                        distance = abs(goal_row - cur_row) + abs(goal_col - cur_col)
                        h_score = h_score + distance
            return h_score
        else:
            # Count misplaced tiles
            for row in range(0, self.size):
                for col in range(0, self.size):
                    if self.board[row][col] != self.goal_board[row][col] and self.board[row][col] != 0:
                        h_score = h_score + 1
            return h_score

    def possible_next_states(self, h_method=None):
        # find the empty tile
        (row_0, col_0) = self.find_position_of_tile(self.board, 0)

        # find valid move
        valid_moves = []
        # move up
        if row_0 - 1 >= 0:
            valid_moves.append((row_0 - 1, col_0, 'up'))
        # move down
        if row_0 + 1 < self.size:
            valid_moves.append((row_0 + 1, col_0, 'down'))
        # move left
        if col_0 - 1 >= 0:
            valid_moves.append((row_0, col_0 - 1, 'left'))
        # move right
        if col_0 + 1 < self.size:
            valid_moves.append((row_0, col_0 + 1, 'right'))

        # move and create next states
        next_states = []
        for move in valid_moves:
            # copy original board
            next_board = [x[:] for x in self.board]
            
            # swap empty tile
            original_value = next_board[move[0]][move[1]]
            next_board[row_0][col_0] = original_value
            next_board[move[0]][move[1]] = 0
            next_states.append(State(self.goal_board, next_board, self.g_score + 1, move[2],  self, h_method))
        return next_states
 

        
        