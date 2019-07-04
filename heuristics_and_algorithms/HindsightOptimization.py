import time
import numpy as np
from data_structure.HopRollout import HopRollout

# A* instead of dijkstra?


class HopEdge:
    def __init__(self, start, end, cost, probability):
        self.start = start
        self.end = end
        self.cost = cost
        self.probability = probability
        self.traversable = None

    def is_traversable(self):
        if self.traversable is None:
            self.traversable = np.random.uniform() > self.probability
        return self.traversable

    def reset_traversable(self):
        self.traversable = None

    def __eq__(self, other):
        return self.end == other.end and self.start == other.start

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self.start) + " ---" + self.cost + "--> " + str(self.end)


class HopNode:
    def __init__(self, name, index):
        self.is_start = False
        self.name = name
        self.index = index
        self.output_edges = []
        self.cost_to_come = float('inf')
        self.prev_dijkstra = None
        self.was_rollout_start = False

    def add_edge(self, edge):
        if edge.start == self:
            if any(map((lambda a: a.end == edge.end), self.output_edges)):
                print("Already connected")
            else:
                self.output_edges.append(edge)

    def get_traversable_edges(self):
        return list(filter(lambda a: a.is_traversable(), self.output_edges))

    def reset_traversable_edges(self):
        self.cost_to_come = float('inf')
        self.prev_dijkstra = None
        map((lambda a: a.reset_traversable()), self.output_edges)

    def reset_dijkstra(self):
        self.prev_dijkstra = None
        if not self.is_start:
            self.cost_to_come = float('inf')

    def reset(self):
        self.reset_traversable_edges()
        self.reset_dijkstra()

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __repr__(self):
        return str(self.index) + "\t" + self.name


def deep_copy(nodes, edges, start, finish):
    new_nodes = []
    new_edges = []
    for node in nodes:
        new_node = HopNode(node.name, node.index)
        new_nodes.append(new_node)

    for edge in edges:
        new_start = first(new_nodes, (lambda a: a == edge.start))
        new_end = first(new_nodes, (lambda a: a == edge.end))
        new_edge = HopEdge(new_start, new_end, edge.cost, edge.probability)
        new_edges.append(new_edge)
        new_start.add_edge(new_edge)

    new_start = first(new_nodes, (lambda a: a == start))
    new_finish = first(new_nodes, (lambda a: a == finish))
    return new_nodes, new_edges, new_start, new_finish


class HindsightOptimization:
    def __init__(self, rollouts_amount, nodes, edges, start, finish):
        self.rollouts = []
        self.rollouts_amount = rollouts_amount
        self.nodes = nodes
        self.edges = edges
        self.start = start
        self.finish = finish
        self.ranked_edges = []

    def generate_rollouts_and_find_routes(self):
        for i in range(self.rollouts_amount):
            print("\nRollout: " + str(i + 1))
            new_nodes, new_edges, new_start, new_finish = deep_copy(self.nodes, self.edges, self.start, self.finish)
            rollout = HopRollout(new_start, new_finish, new_nodes, new_edges)
            rollout.find_routes()
            rollout.reset_all_nodes_edges()
            self.rollouts.append(rollout)

    def generate_edge_ranking(self):
        ranking = []
        for i in range(len(self.start.output_edges)):
            ranking.append((self.start.output_edges[i], []))
            for rollout in self.rollouts:
                current_edge = self.start.output_edges[i]
                index = index_of_route_starting_from_edge(rollout.routes_per_edge, current_edge.end)
                if index > -1:
                    ranking[i][1].append(rollout.routes_per_edge[index].full_cost + current_edge.cost)

        for i in range(len(ranking)):
            appearance_amount = len(ranking[i][1])
            if appearance_amount == 0:
                ranking[i] = (ranking[i][0], float('inf'))
            else:
                ranking[i] = (ranking[i][0], sum(ranking[i][1])/appearance_amount)

        self.ranked_edges = sorted(ranking, key=(lambda tup: tup[1]))

    def hindsight_optimization_runner(self):
        run_nodes, run_edges, run_start, run_finish = deep_copy(self.nodes, self.edges, self.start, self.finish)
        full_path = [self.start]
        full_cost = 0
        times = []
        while self.start != run_finish:
            start_time = time.time()
            self.generate_rollouts_and_find_routes()
            self.generate_edge_ranking()
            used_edge_tuple = first(
                self.ranked_edges,
                key=(lambda edge_tup:
                     edge_tup[0] in self.start.get_traversable_edges()
                     and edge_tup[1] < float('inf'))
            )
            if used_edge_tuple is None:
                return -1, [], -1, -1
            self.start.reset_dijkstra()
            self.start.reset_traversable_edges()
            self.start = used_edge_tuple[0].end
            full_path.append(self.start)
            full_cost += used_edge_tuple[0].cost
            times.append(time.time() - start_time)

        return full_cost, full_path, sum(times), sum(times)/(len(times) + 1e-6)


def first(elements, key):
    for element in elements:
        if key(element):
            return element


def index_of_route_starting_from_edge(elements, el):
    result = -1
    for i in range(len(elements)):
        route = elements[i].route
        if len(route) > 0 and route[0] == el:
            result = i
            break
    return result

# End of file
