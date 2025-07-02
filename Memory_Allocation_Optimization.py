from itertools import combinations

def optimize_memory(blocks, k, max_memory):
    max_sum = 0
    best_blocks = None
    for combo in combinations(blocks, k):
        curr_sum = sum(combo)
        if curr_sum <= max_memory and curr_sum > max_sum:
            max_sum = curr_sum
            best_blocks = combo
    return list(best_blocks) if best_blocks else [], max_sum

# Example
blocks = [100, 200, 150, 50, 300, 75, 125]
k, max_memory = 3, 500
selected, total = optimize_memory(blocks, k, max_memory)
print(f"Blocks: {selected}, Total Memory: {total}")
