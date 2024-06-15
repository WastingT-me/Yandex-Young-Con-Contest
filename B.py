# -*- coding: utf-8 -*-

def min_window_cost(n, k, crystals):
    from collections import defaultdict

    # Dictionary to keep track of the count of each crystal type
    count = defaultdict(int)
    # Total cost of the current window
    current_cost = 0

    required_types = set(range(1, k + 1))
    min_cost = float('inf')
    left = 0
    unique_count = 0

    for right in range(n):
        crystal = crystals[right]
        if crystal in required_types:
            if count[crystal] == 0:
                unique_count += 1
            count[crystal] += 1
        current_cost += crystal

        while unique_count == k:
            min_cost = min(min_cost, current_cost)

            left_crystal = crystals[left]
            current_cost -= left_crystal
            if left_crystal in required_types:
                count[left_crystal] -= 1
                if count[left_crystal] == 0:
                    unique_count -= 1
            left += 1

    return min_cost if min_cost != float('inf') else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])
    crystals = list(map(int, data[2:]))

    result = min_window_cost(n, k, crystals)
    print(result)

if __name__ == "__main__":
    main()