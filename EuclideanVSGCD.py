import random
from time import time
import matplotlib.pyplot as plt


#Euclidean
def euclidean(a, b):
    if (a == 0):
        return b
    return euclidean(b % a, a)


#GCD
def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)


if __name__ == '__main__':
    x_axis = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
    euclidean_point = []
    gcd_point = []
    print("Euclidean" + "             GCD")
    for i in range(0, 10):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        init = time()
        for i in range(0, 100000):
            euclidean(num1, num2)
        euclidean_time = time() - init
        euclidean_point.append(euclidean_time)
        # print(x_axis)
        init = time()
        for i in range(0, 100000):
            gcd(num1, num2)
        gcd_time = time() - init
        gcd_point.append(gcd_time)
        print(str(euclidean_time) + "   " + str(gcd_time))
    plt.plot(x_axis, euclidean_point, label="Euclidean", marker="o")
    plt.plot(x_axis, gcd_point, label="GCD", marker="o")
    plt.xlabel('x_axis')
    # plt.ylabel('')
    plt.title('Euclidean Vs General GCD')
    plt.legend()
    plt.show()
