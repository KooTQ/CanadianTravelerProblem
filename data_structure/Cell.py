import numpy as np


class Cell:
    def __init__(self, name, staying_cost=-1):
        self.staying_cost = staying_cost
        self.connections = []
        self.name = name

    def add_connection(self, connection):
        if all(map(lambda a: a.get_end_cell() != connection, self.connections)):
            self.connections.append(connection)
        else:
            print("Already connected!")

    def get_currently_viable_connections(self, prev_cell):
        viable_connections = []
        for connection in self.connections:
            rand_number = np.random.random_sample()
            if rand_number < connection.probability:
                viable_connections.append(connection)
            elif prev_cell == connection.end_cell:
                viable_connections.append(connection)
        return viable_connections

    def get_all_connections(self):
        return self.connections

    def get_all_connected_cells(self):
        result = []
        if self.staying_cost >= 0:
            result.append(self)
        map(lambda a: result.append(a.get_end_cell()), self.connections)
        return result

    def get_name(self):
        return self.name

# end of file
