from time import time

V = 4  #Number of vertices

INF = 99999


def floydWarshall(graph):

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1],
         [INF, INF, INF, 0]]

init = time()
for i in range(1000):
    floydWarshall(graph)
print(time() - init)
