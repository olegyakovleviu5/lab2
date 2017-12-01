import random


def arr_min(arr):
    mini = arr[0]

    for i in range(1, len(arr) - 1):
        if arr[i] < mini:
            mini = arr[i]
    return mini


def avg(arr):
    summ = 0
    for x in arr:
        summ += x
    summ /= len(arr)
    return summ

array = [4, 7, 8, 1, 3, 0, 3, -5, 1];
print(array)
print(arr_min(array))
print(avg(array))