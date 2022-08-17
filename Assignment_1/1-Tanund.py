def insertion_sort(input_list):
    # iterate through the list starting from second value
    for i_pick in range(1, len(input_list)):
        picked_value = input_list[i_pick]
        insert_idx = i_pick
        # iterate from previous index of picked value to the first index of the list
        for i_comp in range(i_pick - 1, -1, -1):
            if picked_value < input_list[i_comp]:
                # shift compared value to the right
                input_list[i_comp + 1] = input_list[i_comp]
                insert_idx = i_comp
            else:
                # exit the loop if picked value is greater than the value on the left
                break
        # insert the picked value at correct index
        input_list[insert_idx] = picked_value
    return input_list

print("Testing Insertion Sort")
print("=============================")
test_list = [6, 5, 3, 4, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(insertion_sort(test_list)))

test_list = [1, 5, 4, 1, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(insertion_sort(test_list)))

print("=============================")


def merge_sort(input_list, start_index, last_index):
    if start_index < last_index:
        mid_index = (start_index + last_index) // 2 # floor rounding
        merge_sort(input_list, start_index, mid_index)
        merge_sort(input_list, mid_index + 1, last_index)
        merge(input_list, start_index, mid_index, last_index)
    return input_list

def merge(input_list, start_index, mid_index, last_index):
    # split the input list
    first_half_list = input_list[start_index : mid_index + 1]
    second_half_list = input_list[mid_index + 1 : last_index + 1]
    i_first = 0
    i_second = 0
    # rearrange the input list
    for i_merge in range(start_index, last_index + 1):
        # if one of splitted lists reaches its end, use value from another list to fill input list
        if i_first == len(first_half_list):
            input_list[i_merge] = second_half_list[i_second]
            i_second += 1
        elif i_second == len(second_half_list):
            input_list[i_merge] = first_half_list[i_first]
            i_first += 1
        # if not, do the comparision and put it in order
        else:
            if first_half_list[i_first] <= second_half_list[i_second]:
                input_list[i_merge] = first_half_list[i_first]
                i_first += 1
            else:
                input_list[i_merge] = second_half_list[i_second]
                i_second += 1

print("Testing Merge Sort")
print("=============================")

test_list = [6, 5, 3, 4, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(merge_sort(test_list, 0, len(test_list) - 1)))

test_list = [7, 6, 5, 4, 3, 2, 3]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(merge_sort(test_list, 0, len(test_list) - 1)))

test_list = [1, 5, 4, 1, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(merge_sort(test_list, 0, len(test_list) - 1)))
print("=============================")
