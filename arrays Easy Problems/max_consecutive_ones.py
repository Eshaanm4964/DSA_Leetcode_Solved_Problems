def maximum_consecutive_ones(arr):
    n = len(arr)
    count = 0
    max_cons = 0
    for i in range(n):
        if arr[i] == 1:
            count+=1
            max_cons = max(count,max_cons)
        else:
            count = 0
    return max_cons

arr = [1, 0, 1, 1, 0, 1]
print(maximum_consecutive_ones(arr))

