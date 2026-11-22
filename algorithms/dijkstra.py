
# MINI-COURIER PLANNER
# DIJKSTRA'S SHORTEST PATH ALGORITHM

import time
import heapq

graph = {
    "Warehouse": {"A": 4, "B": 2},
    "A": {"Warehouse": 4, "B": 1, "C": 5},
    "B": {"Warehouse": 2, "A": 1, "C": 8, "D": 10},
    "C": {"A": 5, "B": 8, "D": 2},
    "D": {"B": 10, "C": 2}
}


def dijkstra(graph, start_node):

    start = time.perf_counter()

    distances = {
        node: float("inf") for node in graph
    }

    distances[start_node] = 0

    previous = {}
    priority_queue = [(0, start_node)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    end = time.perf_counter()

    print("\n===== DIJKSTRA SHORTEST PATH =====")

    for node, distance in distances.items():
        print(start_node, "to", node, "=", distance, "km")

    print("\nExecution Time:",
          round(end - start, 6), "seconds")

    return distances, previous


if __name__ == "__main__":
    dijkstra(graph, "Warehouse")
