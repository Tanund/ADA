import random
import time
import matplotlib.pyplot as plt
import math


def max_crossing_subarray(input_list, low, mid, high):
    sum = 0
    left_sum = float('-inf')
    for i in range(mid, low - 1, -1):
        sum = sum + input_list[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    right_sum = float('-inf')
    for i in range(mid + 1, high + 1):
        sum = sum + input_list[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum

def max_subarray(input_list, low, high):
    if high == low:
        return low, high, input_list[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(input_list, low, mid)
        right_low, right_high, right_sum = max_subarray(input_list, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(input_list, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


print("========== Testing ============")
input_list = [-5, 1, 2, 9, -5, 8]
low, high, sum = max_subarray(input_list, 0, len(input_list) - 1)
print("Input: " + str(input_list))
print("low: " + str(low) + ", high: " + str(high) + ", sum: " + str(sum))

input_list = []
# for loop and append 10 input
for i in range(0, 10):
    input_list.append(random.randrange(-10, 11))
low, high, sum = max_subarray(input_list, 0, len(input_list) - 1)
print("Input: " + str(input_list))
print("low: " + str(low) + ", high: " + str(high) + ", sum: " + str(sum))

print("========== Plot graph ============")
number_of_n = [5000, 10000, 50000, 100000, 150000, 200000, 250000, 300000]
result_time = []
theory_time = []
for each_n in number_of_n:
    input_list = []
    for i in range(0, each_n):
        input_list.append(random.randrange(-10, 11))
    start_time = time.process_time()
    low, high, sum = max_subarray(input_list, 0, each_n - 1)
    stop_time = time.process_time()
    result_time.append(stop_time - start_time)
    print("Number of n: " + str(each_n))
    print("Process time: " + str(stop_time - start_time) + " seconds" )

    cost = 1/1000000
    theory_time.append(cost * each_n * math.log2(each_n))

plt.title("Maximum sub array problem")
plt.xlabel("number of inputs")
plt.ylabel("time (ms)")
plt.plot(number_of_n, result_time, marker="o", color="red", label="code")
plt.plot(number_of_n, theory_time, marker="o", color="blue", label="theory")
plt.grid()
plt.legend()
plt.show()