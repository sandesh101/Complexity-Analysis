import sys
import random
from time import time
import matplotlib.pyplot as plt


def MatrixChainOrder(p, i, j):

    if i == j:
        return 0

    _min = sys.maxsize

    for k in range(i, j):

        count = (MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j) +
                 p[i - 1] * p[k] * p[j])

        if count < _min:
            _min = count

    return _min


arr = []
matrixchain_point = []
for i in range(0, 10):
    ran_num = random.randint(1, 1000)
    arr.append(ran_num)
    # print(arr)
    init = time()
    for i in range(0, 10000):
        MatrixChainOrder(arr, 1, len(arr) - 1)
    matrixchain_time = time() - init
    matrixchain_point.append(matrixchain_time)
    print(matrixchain_time)

#Graph Plotting
plt.plot(arr,
         matrixchain_point,
         label="Matrix chain multiplication",
         marker="o")
plt.xlabel('Size')
plt.title('Matrix chain multiplication')
plt.legend()
plt.show()

# n = len(arr)

# print("Minimum number of multiplications is ", MatrixChainOrder(arr, 1, n - 1))
