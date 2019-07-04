import numpy as np

stay_in_city_cost = -2
# stay_in_city_cost = 50
size = 12
input_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\uk12\\uk12_dist.txt"
output_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\uk12\\uk12_only_direct_no_loops_dist.txt"
# output_path = "C:\\Uczelnia\\SI2\\CanadianTravelerProblem\\datasets\\uk12\\uk12_only_direct_loops_dist.txt"
with open(input_path, "r") as file:
    lines = file.readlines()

data = []
for line in lines:
    if '#' not in line:
        row = []
        split_lines = line.split()
        for s_line in split_lines:
                row.append(float(s_line))
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
                        reconstructed_data[x][y1] = -1

for x in range(size):
    for y in range(size):
        if x != y and reconstructed_data[x][y] != -1:
            reconstructed_data[x][y] = data[x][y]

result = []
for x in range(size):
    print(reconstructed_data[x].tolist())
    row = ""
    for item in reconstructed_data[x].tolist():
        row = row + " " + str(item)
    row = row + "\n"
    result.append(row)

with open(output_path, "w+") as file:
    file.writelines(result)


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
