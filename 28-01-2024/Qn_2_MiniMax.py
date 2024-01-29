def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(f"{min_sum} {max_sum}")
