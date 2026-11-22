
# MINI-COURIER PLANNER
# Dynamic Programming - 0/1 Knapsack

import time

def knapsack(parcels, capacity):

    start = time.perf_counter()

    n = len(parcels)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        priority = parcels[i - 1]["priority"]

        for w in range(capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    priority + dp[i - 1][w - weight],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    end = time.perf_counter()

    print("\n===== OPTIMIZED PACKING PLAN =====")

    for parcel in selected:
        print(parcel["name"], "- Weight:", parcel["weight"])

    print("\nMaximum Priority:", dp[n][capacity])

    print("Total Weight:",
          sum(p["weight"] for p in selected))

    print("Execution Time:",
          round(end - start, 6), "seconds")

    return selected


if __name__ == "__main__":

    parcels = [
        {"id": 101, "name": "Books", "weight": 3, "priority": 5},
        {"id": 102, "name": "Laptop", "weight": 5, "priority": 10},
        {"id": 103, "name": "Clothes", "weight": 2, "priority": 4},
        {"id": 104, "name": "Shoes", "weight": 4, "priority": 7},
        {"id": 105, "name": "Documents", "weight": 1, "priority": 9}
    ]

    knapsack(parcels, 10)
