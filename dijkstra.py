from time import time


def dijkstra(nodes, edges, source_index=0):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0

    adjacent_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv
        adjacent_nodes[v][u] = w_uv
    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        {v: path_lengths[v] for v in temporary_nodes}
        temporary_nodes.remove(u)
        for v, w_uv in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)
    return path_lengths


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6]
    edges = {
        (1, 2): 1.0,
        (1, 3): 3.0,
        (1, 4): 2.0,
        (2, 3): 3.0,
        (2, 4): 6.0,
        (3, 4): 7.0,
        (4, 5): 3.0,
        (5, 6): 5.0
    }
    source_index = 0
    init = time()
    for i in range(0, 10000):
        dijkstra(nodes, edges, source_index)
    print(time() - init)