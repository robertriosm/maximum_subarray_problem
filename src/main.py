from timeit import default_timer
import divide_and_conquer
import dynamic_programming

array = [-2, -3, 4, -1, -2, 1, 5, -3]

print(divide_and_conquer.find_maximum_subarray(array))
print(dynamic_programming.find_maximum_subarray(array))
