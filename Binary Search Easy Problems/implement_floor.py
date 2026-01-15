def find_floor(arr,x):
    n = len(arr)
    low = 0
    high = n-1
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=x:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return ans 