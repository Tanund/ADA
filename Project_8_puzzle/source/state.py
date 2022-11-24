class State:
    def __init__(self, goal_board, board, g_score, parent_state=None):
        self.board = board
        self.goal_board = goal_board
        self.size = len(board)
        self.parent_state = parent_state
        self.g_score = g_score
        self.h_score = self.calculate_h()
        self.f_score = self.g_score + self.h_score

    def calculate_h(self):
        """Count misplaced tiles"""
        h_score = 0
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.board[row][col] != self.goal_board[row][col] and self.board[row][col] != 0:
                    h_score = h_score + 1
        return h_score

    def possible_next_states(self):
        # find the empty tile
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.board[row][col] == 0:
                    row_0 = row
                    col_0 = col

        # find valid move
        valid_moves = []
        # move up
        if row_0 - 1 >= 0:
            valid_moves.append((row_0 - 1, col_0))
        # move down
        if row_0 + 1 < self.size:
            valid_moves.append((row_0 + 1, col_0))
        # move left
        if col_0 - 1 >= 0:
            valid_moves.append((row_0, col_0 - 1))
        # move right
        if row_0 + 1 < self.size:
            valid_moves.append((row_0, col_0 + 1))

        # move and create next states
        next_states = []
        for move in valid_moves:
            # copy original board
            next_board = [x[:] for x in self.board]
            
            # swap empty tile
            original_value = next_board[move[0]][move[1]]
            next_board[row_0][col_0] = original_value
            next_board[move[0]][move[1]] = 0
            next_states.append(State(self.goal_board, next_board, self.g_score + 1, self))
        return next_states



        
        