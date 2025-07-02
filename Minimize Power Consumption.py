from itertools import combinations

def minimize_power(tasks, k, target):
    closest_sum = 0
    best_tasks = None
    for combo in combinations(tasks, k):
        curr_sum = sum(combo)
        if curr_sum <= target and curr_sum > closest_sum:
            closest_sum = curr_sum
            best_tasks = combo
    return list(best_tasks) if best_tasks else [], closest_sum

# Example
tasks = [30, 50, 20, 60, 10, 25]
k, target = 2, 100
selected, total = minimize_power(tasks, k, target)
print(f"Tasks: {selected}, Total Power: {total}")
