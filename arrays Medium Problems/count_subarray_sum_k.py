def subarray_sum_count_sum_k(arr,k):
    n = len(arr)
    count = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i,n):
            total+=arr[i]

            if total ==k:
                count+=1

    return count

