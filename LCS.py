from time import time
# import matplotlib.pyplot as plt


def lcs(X, Y, m, n):

    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


X = "ABCDEFGHI"
Y = "CDEFG"
# x_axis = [1, 2, 3, 4, 5, 6]
init = time()
for i in range(0, 10000):
    lcs_time = lcs(X, Y, len(X), len(Y))
print(lcs_time)
# lcs_plot = lcs_time

# plt.plot(x_axis, lcs_plot)
# plt.show()