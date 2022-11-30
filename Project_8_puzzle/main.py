from source.state import State
import os
from source.search_functions import A_star, Dijkstra, BFS, DFS
from treelib import Node, Tree


def print_result(final_state:State, file_path, tree:Tree=None):
    parent = final_state.parent_state
    list_state = [final_state]
    while parent:
        list_state.append(parent)
        parent = parent.parent_state
    list_state.reverse()

    all_moves = ",".join([x.action for x in list_state if x.action])
    with open(file_path, 'w') as f:
        print('------Summary---------')
        f.write('------Summary---------'+ '\n')
        print('Number of loops: ' + str(count)+ '\n')
        f.write('Number of loops: ' + str(count)+ '\n')
        print('Running time: ' + str(running_time)+ '\n')
        f.write('Running time: ' + str(running_time)+ '\n')
        print('Max level: ' + str(max_level)+ '\n')
        f.write('Max level: ' + str(max_level)+ '\n')
        print('Remaining states: ' + str(remaining_state)+ '\n')
        f.write('Remaining states: ' + str(remaining_state)+ '\n')
        f.write('Moves to take: ' + all_moves + '\n')
        
        f.write('\n-------------Tree------------\n')
    if tree:
        tree.save2file(file_path)
    with open(file_path, 'a') as f:

        for i in range(len(list_state)):
            # print('----------------------------')
            f.write('----------------------------\n')
            if i == 0:
                # print('Step: ' + str(i) + ' --> Initial board')
                f.write('Step: ' + str(i) + ' --> Initial board\n')
            elif i == len(list_state) - 1:
                # print('Step: ' + str(i) + ' --> Goal board')
                f.write('Step: ' + str(i) + ' --> Goal board\n')
            else:
                # print('Step: ' + str(i))
                f.write('Step: ' + str(i) + '\n')

            # print('Action: ' + str(list_state[i].action))
            f.write('Action: ' + str(list_state[i].action) + '\n')
            # print('Level: ' + str(list_state[i].g_score))
            f.write('Level: ' + str(list_state[i].g_score) + '\n')
            for row in list_state[i].board:
                # print(row)
                f.write(str(row) + '\n')

def isSolvable_new(init, goal) :
    
    # Count inversions in given 8 puzzle
    init = [j for sub in init for j in sub]
    goal = [j for sub in goal for j in sub]

    init_set = set()
    goal_set = set()
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if init[j] != empty_value and init[i] != empty_value:
                init_set.add((init[i], init[j]))

    for i in range(0, 9):
        for j in range(i + 1, 9):
            if goal[j] != empty_value and goal[i] != empty_value:
                goal_set.add((goal[i], goal[j]))

    unique = init_set - goal_set
    inversion = len(unique)
    inv_count = 0
    for i in range(0, 9):
        if init[i] != empty_value and goal[i] != empty_value and init[i] > goal[i]:
            inv_count += 1 
    # return true if inversion count is even
    return (inversion % 2 == 0)

if __name__ == '__main__':
    dir = os.path.dirname(__file__) + '\\output'
    goal_board = [
        [1,2,3],
        [8,0,4],
        [7,6,5]
        ]
    init_board = [
        [2,8,3],
        [1,6,4],
        [7,0,5]
        ]
    if(isSolvable_new(init_board, goal_board)):
        print("Solvable")
    else :
        print("Not Solvable")
        exit()
    init_state = State(goal_board, init_board, 0)
    
    print('Running A_star')
    (final_state, count, running_time, max_level, remaining_state, tree) = A_star(init_state)
    if final_state:
        print_result(final_state, dir + '\\A_star.txt', tree)

    print('Running A_star Manhattan')
    (final_state, count, running_time, max_level, remaining_state, tree) = A_star(init_state, 'mht')
    if final_state:
        print_result(final_state, dir + '\\A_star_mht.txt', tree)

    print('Running Dijkstra')
    (final_state, count, running_time, max_level, remaining_state, tree) = Dijkstra(init_state)
    if final_state:
        print_result(final_state, dir + '\\Dijkstra.txt', tree)
    
    print('Running BFS')
    (final_state, count, running_time, max_level, remaining_state, tree) = BFS(init_state)
    if final_state:
        print_result(final_state, dir + '\\BFS.txt', tree)

    print('Running DFS')
    (final_state, count, running_time, max_level, remaining_state, tree) = DFS(init_state)
    if final_state:
        print_result(final_state, dir + '\\DFS.txt')

