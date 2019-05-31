import numpy as np

dist_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\usca312\\usca312_only_direct_dist_reconstructed.txt"
# dist_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\usca312\\usca312_only_direct_loops_dist.txt"
names_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\usca312\\usca312_name.txt"
max_value = 1e9


def load_nodes(probability_func, size, node_type):
    with open(dist_path, 'r') as data_file:
        lines = data_file.readlines()

    distances_matrix = np.ones((size, size), dtype='int64') * max_value

    for x in range(size):
        s_line = lines[x].split()
        for y in range(size):
            dist = float(s_line[y])
            if dist < 0:
                dist = max_value
            distances_matrix[x][y] = dist

    del lines
    with open(names_path, 'r') as data_file:
        names = list(map(lambda a: a.split('\n')[0].replace(',', ':'), filter(lambda a: a[0] != "#", data_file.readlines())))

    nodes = []
    for x in range(size):
        # node = Node(names[x], x, staying_cost=distances_matrix[x][x])
        node = node_type(names[x], x, staying_cost=distances_matrix[x][x])
        nodes.append(node)

    for x in range(size):
        for y in range(size):
            if 0 <= distances_matrix[x][y] < max_value:
                nodes[x].add_edge(nodes[y], distances_matrix[x][y], probability_func(distances_matrix, x, y))

    return nodes

# End of file
