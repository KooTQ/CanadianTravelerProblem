import numpy as np
from heuristics_and_algorithms.probability_functions import random

prob_function = random
input_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\kn57\\kn57_"
stay_in_city_cost, output_dist, size = -2, \
                                       input_path + "only_direct_dist_reconstructed.txt", \
                                       57

input_dist_path = input_path + "dist.txt"
output_prob_path = input_path + "prob.txt"
output_connections_path = input_path + "connections.txt"

CONNECTED = 1
NOT_CONNECTED = -1
LOOP = -2

with open(input_dist_path, "r") as file:
    lines = file.readlines()

data = []
row = []
counter = 0
for line in lines:
    if '#' not in line:
        split_lines = line.split()
        for s_line in split_lines:
            if counter == size:
                data.append(row)
                row = []
                counter = 0
            row.append(float(s_line))
            counter += 1
if len(data) + 1 == size:
    data.append(row)

for x in range(size):
    for y in range(size):
        if data[x][y] != data[y][x]:
            print("Unsymmetrical: ", x, y)

reconstructed_data = np.ones((size, size)) * stay_in_city_cost
for x in range(size):
    for y in range(size):
        if x != y:
            for y1 in range(size):
                if x != y1 and y != y1:
                    if data[x][y] + data[y][y1] == data[x][y1]:
                        reconstructed_data[x][y1] = NOT_CONNECTED

for x in range(size):
    for y in range(size):
        if x != y and reconstructed_data[x][y] != NOT_CONNECTED:
            reconstructed_data[x][y] = data[x][y]

result_dist = []
for x in range(size):
    row = ""
    for item in reconstructed_data[x].tolist():
        row = row + " " + str(item)
    row = row + "\n"
    result_dist.append(row)

with open(output_dist, "w+") as file:
    file.writelines(result_dist)

result_connections = []
for x in range(size):
    for y in range(size):
        connection_flag = None
        if x == y:
            connection_flag = LOOP
        elif reconstructed_data[x][y] == NOT_CONNECTED:
            connection_flag = NOT_CONNECTED
        else:
            connection_flag = CONNECTED
        row = str(x) + " " + str(y) + " " + str(connection_flag) + "\n"
        result_connections.append(row)

with open(output_connections_path, "w+") as file:
    file.writelines(result_connections)

result_prob = []
for x in range(size):
    row = ""
    for y in range(size):
        if x != y:
            prob = prob_function(reconstructed_data, x, y)
        else:
            prob = 0
        row = row + " " + str(prob)
    row = row + "\n"
    result_prob.append(row)

with open(output_prob_path, "w+") as file:
    file.writelines(result_prob)

# End of file
