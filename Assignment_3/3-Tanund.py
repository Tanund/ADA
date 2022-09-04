from distutils.command.build import build


def max_heapify(input_list, current_index, heap_size):

    child_left_index = get_child_left_index(current_index)
    child_right_index = get_child_right_index(current_index)

    if child_left_index <= heap_size and input_list[child_left_index - 1] > input_list[current_index - 1]:
        largest = child_left_index
    else:
        largest = current_index
    if child_right_index <= heap_size and input_list[child_right_index - 1] > input_list[largest - 1]:
        largest = child_right_index

    if largest != current_index:
        tmp = input_list[current_index - 1]
        input_list[current_index - 1] = input_list[largest - 1]
        input_list[largest - 1] = tmp
        max_heapify(input_list, largest, heap_size)

def build_max_heap(input_list):
    heap_size = len(input_list)
    for i in range((heap_size // 2), 0, -1):
        max_heapify(input_list, i, heap_size)

def heap_sort(input_list):
    heap_size = len(input_list)
    build_max_heap(input_list)
    for i in range(len(input_list), 1, -1):
        tmp = input_list[i - 1]
        input_list[i - 1] = input_list[0]
        input_list[0] = tmp

        heap_size = heap_size - 1
        max_heapify(input_list, 1, heap_size)

    return input_list

def get_parent_index(current_index):
    return current_index // 2

def get_child_left_index(current_index):
    return current_index * 2

def get_child_right_index(current_index):
    return (current_index * 2) + 1

print("Testing Heap Sort")
print("=============================")
test_list = [6, 5, 3, 4, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(heap_sort(test_list)))

test_list = [1, 5, 4, 1, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(heap_sort(test_list)))