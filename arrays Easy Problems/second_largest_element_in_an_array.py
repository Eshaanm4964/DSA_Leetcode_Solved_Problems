def second_largest(arr):
    second_largest = float("-inf")
    largest = float("-inf")
    for i in range(len(arr)):
        if arr[i]>largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest = arr[i]
    return second_largest