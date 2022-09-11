def partition(input_list, i_left, i_right):
    middle_man = input_list[i_right - 1]
    i_smaller_part = i_left - 1
    for i_pointer in range(i_left, (i_right - 1) + 1):
        if input_list[i_pointer - 1] <= middle_man:
            i_smaller_part += 1
            # exchange
            tmp = input_list[i_pointer - 1]
            input_list[i_pointer - 1] = input_list[i_smaller_part - 1]
            input_list[i_smaller_part - 1] = tmp
    # exchange
    tmp = input_list[i_smaller_part + 1 - 1]
    input_list[i_smaller_part + 1 - 1] = middle_man
    input_list[i_right - 1] = tmp
    return i_smaller_part + 1

def quick_sort(input_list, i_left, i_right):
    if i_left < i_right:
        i_middle = partition(input_list, i_left, i_right)
        quick_sort(input_list, i_left, i_middle - 1)
        quick_sort(input_list, i_middle + 1, i_right)
    return input_list

print("Testing Quick Sort")
print("=============================")
test_list = [6, 5, 3, 4, 2, 1]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(quick_sort(test_list, 1, len(test_list))))

test_list = [2, 8, 7, 1, 3, 5, 6, 4]
print("Tested list: " + str(test_list))
print("Sorted list: " + str(quick_sort(test_list, 1, len(test_list))))

print("=============================")
        