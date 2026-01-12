def left_rotate_array(arr):
    n = len(arr)
    temp = [0]*n
    for i in range(i,n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]
