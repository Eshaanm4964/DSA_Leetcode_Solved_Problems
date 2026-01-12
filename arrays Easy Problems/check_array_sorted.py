def check_sorted(arr):
    n =len(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                return True 
    return False