from source.state import State
from source.search_functions import A_star, Dijkstra, BFS, DFS

def print_state(final_state:State):
    parent = final_state.parent_state
    list_state = [final_state]
    while parent:
        list_state.append(parent)
        parent = parent.parent_state
    list_state.reverse()
    for i in range(len(list_state)):
        print('----------------------------')
        if i == 0:
            print('Step: ' + str(i) + ' --> Initial board')
        elif i == len(list_state) - 1:
            print('Step: ' + str(i) + ' --> Goal board')
        else:
            print('Step: ' + str(i))

        print('Action: ' + str(list_state[i].action))
        print('Level: ' + str(list_state[i].g_score))
        print_board(list_state[i].board)

def print_board(board):
    for row in board:
        print(row)

def isSolvable_new(init, goal) :
    
    # Count inversions in given 8 puzzle
    init = [j for sub in init for j in sub]
    goal = [j for sub in goal for j in sub]

    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        if init[i] > goal[i]:
        # if init[i] != empty_value and goal[i] != empty_value and init[i] > goal[i]:
            inv_count += 1 
    # return true if inversion count is even
    return (inv_count % 2 == 0)

if __name__ == '__main__':
    # goal_board = [
    #     [1,2,3],
    #     [8,0,4],
    #     [7,6,5]
    #     ]
    # init_board = [
    #     [2,8,3],
    #     [1,6,4],
    #     [7,0,5]
    #     ]
    goal_board = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
        ]
    # init_board = [[1, 2, 3],[4, 0, 5],[8, 6, 7]]
    init_board = [[8, 1, 2],[0, 4, 3],[7, 6, 5]]
    if(isSolvable_new(init_board, goal_board)):
        print("Solvable")
    else :
        print("Not Solvable")
    init_state = State(goal_board, init_board, 0)

    (final_state, count, running_time, max_level, remaining_state) = BFS(init_state)
    
    if final_state:
        print_state(final_state)
        print('------Summary---------')
        print('\n' + 'Number of loops: ' + str(count))
        print('\n' + 'Running time: ' + str(running_time))
        print('\n' + 'Max level: ' + str(max_level))
        print('\n' + 'Remaining states: ' + str(remaining_state))

