
# MINI-COURIER PLANNER
# TSP - NEAREST NEIGHBOR ALGORITHM

import time

graph = {
    "Warehouse": {"A": 4, "B": 2},
    "A": {"Warehouse": 4, "B": 1, "C": 5},
    "B": {"Warehouse": 2, "A": 1, "C": 8, "D": 10},
    "C": {"A": 5, "B": 8, "D": 2},
    "D": {"B": 10, "C": 2}
}


def nearest_neighbor(graph, start_node):

    start = time.perf_counter()

    unvisited = set(graph.keys())
    unvisited.remove(start_node)

    route = [start_node]
    current = start_node
    total_distance = 0

    while unvisited:

        next_node = min(
            unvisited,
            key=lambda node: graph[current].get(
                node, float("inf")
            )
        )

        distance = graph[current].get(next_node, float("inf"))

        if distance == float("inf"):
            break

        total_distance += distance

        route.append(next_node)
        unvisited.remove(next_node)

        current = next_node

    if start_node in graph[current]:

        total_distance += graph[current][start_node]
        route.append(start_node)

    end = time.perf_counter()

    print("\n===== COURIER DELIVERY ROUTE =====")

    print("Route:", " -> ".join(route))

    print("Total Distance:", total_distance, "km")

    print("Execution Time:",
          round(end - start, 6), "seconds")

    return route, total_distance


if __name__ == "__main__":

    nearest_neighbor(graph, "Warehouse")
