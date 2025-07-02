
from itertools import combinations

def closest_subset_sum(readings, k, target):
    closest_sum = float('inf')
    best_subset = None
    for subset in combinations(readings, k):
        curr_sum = sum(subset)
        if abs(curr_sum - target) < abs(closest_sum - target):
            closest_sum = curr_sum
            best_subset = subset
    return list(best_subset), closest_sum

# Example
readings = [10, 15, 20, 25, 30, 5, 8, 12]
k, target = 3, 50
subset, total = closest_subset_sum(readings, k, target)
print(f"Subset: {subset}, Sum: {total}")
