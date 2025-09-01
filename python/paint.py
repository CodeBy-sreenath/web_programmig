def is_possible(A, N, K, mid):
    painters = 1
    curr_sum = 0
    for length in A:
        if curr_sum + length > mid:
            painters += 1
            curr_sum = length
            if painters > K:
                return False
        else:
            curr_sum += length
    return True

def min_time_to_paint(A, N, K):
    low, high = max(A), sum(A)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if is_possible(A, N, K, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# Sample Test
print(min_time_to_paint([10, 10, 10, 10], 4, 2))  # 20
print(min_time_to_paint([10, 20, 30, 40], 4, 2))  # 60
