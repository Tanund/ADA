from heapdict import heapdict
from source.state import State
import time
import queue
from treelib import Node, Tree

def A_star(init_state=State, h_method=None):
    start_time = time.perf_counter()
    tree = Tree()
    tree.create_node(str(init_state.board), str(init_state.board))
    open_state = heapdict()
    visited = []
    open_state[init_state] = init_state.f_score
    count = 0
    max_level = 0
    while open_state:
        if count == 10000:
            print(f"Reach {count} loop --> stop")
            return (None, None, None, None, None, None)
        # pop the lowest f_score (priority)
        popped_item = open_state.popitem()
        current_state = popped_item[0]
        if current_state.h_score == 0:
            running_time = time.perf_counter() - start_time
            return (current_state, count, running_time, max_level, len(open_state), tree)
        visited.append(current_state.board)
        
        count = count + 1
        next_states = current_state.possible_next_states(h_method)
        for each_state in next_states:
            if each_state.board not in visited:
                if not [x for x in open_state.items() if x[0].board == each_state.board]:
                    # added state object as key and f_score as priority
                    open_state[each_state] = each_state.f_score
                    tree.create_node(str(each_state.board) + ' - ' + str(each_state.action), str(each_state.board), parent=str(each_state.parent_state.board))

                    if max_level < each_state.g_score:
                        max_level = each_state.g_score

def Dijkstra(init_state=State):
    start_time = time.perf_counter()
    tree = Tree()
    tree.create_node(str(init_state.board), str(init_state.board))
    open_state = heapdict()
    visited = []
    open_state[init_state] = init_state.f_score
    
    count = 0
    max_level = 0
    while open_state:
        if count == 10000:
            print(f"Reach {count} loop --> stop")
            return (None, None, None, None, None, None)
        # pop the lowest f_score (priority)
        # for same priority it will pop as LIFO queue
        popped_item = open_state.popitem()
        current_state = popped_item[0]
        if current_state.h_score == 0:
            running_time = time.perf_counter() - start_time
            return (current_state, count, running_time, max_level, len(open_state), tree)
        visited.append(current_state.board)

        count = count + 1
        next_states = current_state.possible_next_states()
        for each_state in next_states:
            if each_state.board not in visited:
                if not [x for x in open_state.items() if x[0].board == each_state.board]:
                    # added state object as key and g_score as priority
                    open_state[each_state] = each_state.g_score
                    tree.create_node(str(each_state.board) + ' - ' + str(each_state.action), str(each_state.board), parent=str(each_state.parent_state.board))

                    if max_level < each_state.g_score:
                        max_level = each_state.g_score

def BFS(init_state=State):
    start_time = time.perf_counter()
    tree = Tree()
    tree.create_node(str(init_state.board), str(init_state.board))
    open_state = queue.Queue()
    visited = []
    open_state.put(init_state)
    
    count = 0
    max_level = 0
    while open_state:
        if count == 10000:
            print(f"Reach {count} loop --> stop")
            return (None, None, None, None, None, None)
        # FIFO queue
        popped_item = open_state.get()
        current_state = popped_item
        if current_state.h_score == 0:
            running_time = time.perf_counter() - start_time
            return (current_state, count, running_time, max_level, len(open_state.queue), tree)
        visited.append(current_state.board)

        count = count + 1
        next_states = current_state.possible_next_states()
        for each_state in next_states:
            if each_state.board not in visited:
                if not [x for x in open_state.queue if x.board == each_state.board]:
                    # added state
                    open_state.put(each_state)
                    tree.create_node(str(each_state.board) + ' - ' + str(each_state.action), str(each_state.board), parent=str(each_state.parent_state.board))

                    if max_level < each_state.g_score:
                        max_level = each_state.g_score

def DFS(init_state=State):
    start_time = time.perf_counter()
    tree = Tree()
    tree.create_node(str(init_state.board), str(init_state.board))
    open_state = queue.LifoQueue()
    visited = []
    open_state.put(init_state)
    
    count = 0
    max_level = 0
    while open_state:
        if count == 10000:
            print(f"Reach {count} loop --> stop")
            return (None, None, None, None, None, None)
        # LIFO queue
        popped_item = open_state.get()
        current_state = popped_item
        if current_state.h_score == 0:
            running_time = time.perf_counter() - start_time
            return (current_state, count, running_time, max_level, len(open_state.queue), tree)
        visited.append(current_state.board)

        count = count + 1
        next_states = current_state.possible_next_states()
        for each_state in next_states:
            if each_state.board not in visited:
                if not [x for x in open_state.queue if x.board == each_state.board]:
                    # added state
                    open_state.put(each_state)
                    tree.create_node(str(each_state.board) + ' - ' + str(each_state.action), str(each_state.board), parent=str(each_state.parent_state.board))

                    if max_level < each_state.g_score:
                        max_level = each_state.g_score
