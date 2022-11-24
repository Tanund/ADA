from source.state import State
from source.A_star import A_star

if __name__ == '__main__':
    goal_board = [[1,2,3],[8,0,4],[7,6,5]]
    init_board = [[2,8,3],[1,6,4],[7,0,5]]

    init_state = State(goal_board, init_board, 0)

    final_state: State = A_star(init_state)
    parent = final_state.parent_state
    tmp = [final_state.board]
    while parent:
        parent_board = parent.board
        tmp.append(parent_board)
        parent = parent.parent_state
    tmp.reverse()
    for x in tmp:
        print(x)