from time import time
import random
import matplotlib.pyplot as plt


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = []
    bubble_point = []
    selection_point = []
    insertion_point = []
    print("  Bubble Sort" + "                 Selection Sort" +
          "                 Insertion Sort")
    for i in range(0, 10):
        ran_num = random.randint(1, 1000)
        # key = random.randint(1, 1000)
        arr.append(ran_num)
        # print(arr)
        init = time()
        for i in range(0, 10000):
            bubbleSort(arr)
        bubble_time = time() - init
        bubble_point.append(bubble_time)
        init = time()
        for i in range(0, 10000):
            selectionSort(arr)
        selection_time = time() - init
        selection_point.append(selection_time)
        for i in range(0, 10000):
            insertionSort(arr)
        insertion_time = time() - init
        insertion_point.append(insertion_time)
        print(
            str(bubble_time) + "           " + str(selection_time) +
            "           " + str(insertion_time))
    #Graph Plotting
    plt.plot(arr, bubble_point, label="Bubble Sort", marker="o")
    plt.plot(arr, selection_point, label="Selection Sort", marker="o")
    plt.plot(arr, insertion_point, label="Insertion Sort", marker="o")
    plt.xlabel('Size')
    plt.title('Comparison of different sorting algorithm')
    plt.legend()
    plt.show()
