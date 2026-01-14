def binary_search(arr,x):
    n = len(arr)
    low = 0
    high = n-1

    mid = (low+high)//2

    while low<=high:
        
        if arr[mid]==x:
            return mid
        
        elif arr[mid]>x:
            high = mid-1

        else:
            low = mid+1
    return -1 
        