import random
from time import time
import matplotlib.pyplot as plt


def BinarySearch(arr, l, r, key):
    while (l < r):
        mid = (l + r) / 2
        if key == arr[int(mid)]:
            return mid
        elif key < arr[int(mid)]:
            return BinarySearch(arr, l, mid - 1, key)
        else:
            return BinarySearch(arr, mid + 1, r, key)
    return -1


def SequentialSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == '__main__':
    arr = []
    # size = []
    binary_plot = []
    sequential_plot = []
    print("  Binary Search" + "                 Sequential Search")
    for i in range(0, 10):
        ran_num = random.randint(1, 1000)
        key = random.randint(1, 1000)
        arr.append(ran_num)
        # print(arr)
        init = time()
        for i in range(0, 10000):
            BinarySearch(arr, 0, len(arr) - 1, key)
        binary_time = time() - init
        binary_plot.append(binary_time)
        init = time()
        for i in range(0, 10000):
            SequentialSearch(arr, key)
        sequential_time = time() - init
        sequential_plot.append(sequential_time)
        print(str(binary_time) + "           " + str(sequential_time))

    #Graph Plotting
    plt.plot(arr, binary_plot, label="Binary Search", marker="o")
    plt.plot(arr, sequential_plot, label="Sequential Search", marker="o")
    plt.xlabel('Size')
    plt.title('Binary Vs Sequential Search')
    plt.legend()
    plt.show()