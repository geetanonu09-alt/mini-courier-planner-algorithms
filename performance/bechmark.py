
# MINI-COURIER PLANNER
# PHASE 4: PERFORMANCE TESTING
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import random
import matplotlib.pyplot as plt

from algorithms.sorting import sort_parcels
from algorithms.knapsack import knapsack


# Generate sample datasets

def generate_parcels(size):

    parcels = []

    for i in range(size):

        parcels.append({
            "id": i + 1,
            "name": f"Parcel_{i + 1}",
            "weight": random.randint(1, 10),
            "priority": random.randint(1, 100),
            "deadline": random.randint(1, 20)
        })

    return parcels


# Performance testing

def benchmark():

    sizes = [10, 50, 100, 500, 1000]

    sorting_times = []
    knapsack_times = []

    print("\n===== PERFORMANCE TESTING =====")

    for size in sizes:

        parcels = generate_parcels(size)

        # Sorting performance

        start = time.perf_counter()

        sorted_parcels = sorted(
            parcels,
            key=lambda p: (p["deadline"], -p["priority"])
        )

        sorting_time = time.perf_counter() - start

        sorting_times.append(sorting_time)

        # Knapsack performance

        start = time.perf_counter()

        knapsack(
            parcels,
            50
        )

        knapsack_time = time.perf_counter() - start

        knapsack_times.append(knapsack_time)

        print("\nDataset Size:", size)
        print("Sorting Time:", round(sorting_time, 6), "seconds")
        print("Knapsack Time:", round(knapsack_time, 6), "seconds")

    # Runtime chart

    plt.figure(figsize=(9, 5))

    plt.plot(
        sizes,
        sorting_times,
        marker="o",
        label="Sorting Algorithm"
    )

    plt.plot(
        sizes,
        knapsack_times,
        marker="s",
        label="Knapsack Algorithm"
    )

    plt.xlabel("Number of Parcels")
    plt.ylabel("Execution Time (Seconds)")

    plt.title("Mini-Courier Planner Performance Analysis")

    plt.legend()
    plt.grid(True)

    plt.savefig("performance/runtime_chart.png")

    plt.show()

    print("\nChart saved successfully!")


if __name__ == "__main__":

    benchmark()

