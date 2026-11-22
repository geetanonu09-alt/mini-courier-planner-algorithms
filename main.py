
# MINI-COURIER PLANNER
# Design and Analysis of Algorithms
# Main Application

import time

from algorithms import sorting
from algorithms import knapsack
from algorithms import dijkstra
from algorithms import tsp


def main():

    print("\n" + "=" * 50)
    print("          MINI-COURIER PLANNER")
    print("       DESIGN AND ANALYSIS OF ALGORITHMS")
    print("=" * 50)

    # PHASE 1: PROJECT INFORMATION

    print("\n1. PROJECT INFORMATION")

    print("Total Parcels:", len(sorting.parcels))
    print("Delivery Locations:", list(dijkstra.graph.keys()))

    # PHASE 2: PARCEL SORTING

    print("\n2. PARCEL PRIORITIZATION")

    sorted_parcels = sorting.sort_parcels(
        sorting.parcels
    )

    # PHASE 2: KNAPSACK

    print("\n3. OPTIMIZED PACKAGE SELECTION")

    selected_parcels = knapsack.knapsack(
        sorted_parcels, 10
    )

    # PHASE 3: DIJKSTRA

    print("\n4. SHORTEST DELIVERY PATH")

    distances, previous = dijkstra.dijkstra(
        dijkstra.graph, "Warehouse"
    )

    # PHASE 3: TSP

    print("\n5. DELIVERY ROUTE PLANNING")

    route, distance = tsp.nearest_neighbor(
        tsp.graph, "Warehouse"
    )

    # FINAL SUMMARY

    print("\n" + "=" * 50)
    print("             FINAL SUMMARY")
    print("=" * 50)

    print("Total Parcels:", len(sorting.parcels))

    print("Selected Parcels:", len(selected_parcels))

    print("Selected Parcel Names:")

    for parcel in selected_parcels:
        print("-", parcel["name"])

    print("Delivery Route:", " -> ".join(route))

    print("Total Route Distance:", distance, "km")

    print("\nCOURIER PLANNING COMPLETED!")
    print("=" * 50)


if __name__ == "__main__":
    main()
