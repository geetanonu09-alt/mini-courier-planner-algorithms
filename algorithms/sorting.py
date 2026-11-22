
# MINI-COURIER PLANNER
# Parcel Sorting Algorithm
# Phase 2

import time

parcels = [
    {"id": 101, "name": "Books", "weight": 3, "priority": 5, "deadline": 2},
    {"id": 102, "name": "Laptop", "weight": 5, "priority": 10, "deadline": 1},
    {"id": 103, "name": "Clothes", "weight": 2, "priority": 4, "deadline": 3},
    {"id": 104, "name": "Shoes", "weight": 4, "priority": 7, "deadline": 2},
    {"id": 105, "name": "Documents", "weight": 1, "priority": 9, "deadline": 1}
]


def sort_parcels(parcels):

    start = time.perf_counter()

    sorted_parcels = sorted(
        parcels,
        key=lambda parcel: (parcel["deadline"], -parcel["priority"])
    )

    end = time.perf_counter()

    print("\n===== SORTED PARCELS =====")

    for parcel in sorted_parcels:
        print(
            parcel["id"],
            parcel["name"],
            "Priority:", parcel["priority"],
            "Deadline:", parcel["deadline"]
        )

    print("\nSorting Time:", round(end - start, 6), "seconds")

    return sorted_parcels


if __name__ == "__main__":
    sort_parcels(parcels)
