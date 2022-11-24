from heapdict import heapdict
from source.state import State

def A_star(init_state=State):
    open_state = heapdict()
    visited = set()
    open_state[init_state] = init_state.f_score
    # print(f"open_state: {list(open_state.items())}")
    while open_state:
        popped_item = open_state.popitem()
        current_state = popped_item[0]
        if current_state.h_score == 0:
            return current_state
        visited = tuple(current_state.board)
        # print(visited)

        next_states = current_state.possible_next_states()
        for each_state in next_states:
            if tuple(each_state.board) not in visited:
                open_state[each_state] = each_state.f_score
            else:
                print('wait')
        