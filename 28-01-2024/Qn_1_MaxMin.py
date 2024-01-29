def maxMin(k, arr):
    arr.sort()
    min_unfairness = float('inf')

    for i in range(len(arr) - k + 1):
        current_unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, current_unfairness)

    return min_unfairness

# Sample Input
print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30]))  # Output: 20
print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))  # Output: 3
print(maxMin(2, [1, 2, 1, 2, 1]))  # Output: 0
