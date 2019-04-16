import numpy as np

epsilon = 1.0e-3


def linear(distance_matrix, x, y):
    return 1 - 1 / (distance_matrix[x][y] + epsilon)


def inv_linear(distance_matrix, x, y):
    max_dist = np.max(distance_matrix) + epsilon
    return 1 - 1 / (max_dist - distance_matrix[x][y])


def random(_, _1, _2):
    return np.random.random()


def lower_random(_, _1, _2):
    return np.random.random() * 0.5


def upper_random(_, _1, _2):
    return np.random.random() * 0.5 + 0.5


def lower_linear(distance_matrix, x, y):
    _linear = (1 / (distance_matrix[x][y] + epsilon))
    return _linear / 2


def upper_linear(distance_matrix, x, y):
    _linear = (1 / (distance_matrix[x][y] + epsilon))
    return _linear / 2 + 0.5


def lower_inv_linear(distance_matrix, x, y):
    max_dist = np.max(distance_matrix) + 1
    _inv_linear = 1 / (max_dist - distance_matrix[x][y])
    return _inv_linear / 2


def upper_inv_linear(distance_matrix, x, y):
    max_dist = np.max(distance_matrix) + epsilon
    _inv_linear = 1 / (max_dist - distance_matrix[x][y])
    return _inv_linear / 2 + 0.5


# End of file
