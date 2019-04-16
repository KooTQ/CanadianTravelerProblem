from data_structure.Cell import Cell
from data_structure.Connection import Connection
import numpy as np

dist_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\usca312\\usca312_only_direct_no_loops_dist.txt"
# dist_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\usca312\\usca312_only_direct_loops_dist.txt"
names_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\usca312\\usca312_name.txt"
size = 312
default_quality = 0


def load_cells(probability_func):
    with open(dist_path, 'r') as file:
        lines = file.readlines()

    distances_matrix = np.ones((size, size)) * -1

    for x in range(size):
        s_line = lines[x].split()
        for y in range(size):
            distances_matrix[x][y] = float(s_line[y])

    del lines
    with open(names_path, 'r') as file:
        names = list(filter(lambda a: a[0] != "#", file.readlines()))

    cells = []
    for x in range(size):
        cell = Cell(names[x], staying_cost=distances_matrix[x][x])
        cells.append(cell)

    for x in range(size):
        for y in range(size):
            if distances_matrix[x][y] >= 0:
                cells[x].add_connection(
                    Connection(
                        cells[y],
                        distances_matrix[x][y],
                        probability_func(distances_matrix, x, y),
                        quality=default_quality
                    )
                )

    return cells


# End of file
