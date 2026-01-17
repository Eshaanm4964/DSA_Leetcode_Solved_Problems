def nth_root(n,m):
    low = 1
    high = m
    while low<=high:
        mid = (low+high)//2
        ans = 1
        for _ in range(m):
            ans*=mid
            if ans >m:
                break

            if ans==m:
                return mid 
            
            if ans<m:
                low = mid+1

            else:
                high = mid-1
    return -1 