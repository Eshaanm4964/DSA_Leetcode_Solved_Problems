def sqrt(x):
    if x<2:
        return x
    
    low = 1
    high = x//2
    ans = 0

    while low<=high:
        mid = (low+high)//2
        if mid*mid <=x:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans 

