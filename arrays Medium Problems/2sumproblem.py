#Method-1

def two_sum_problem(arr,target):
    n = len(arr)
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return arr[i],arr[j]
    return None 

#Method-2 

def two_sum_problem(arr,target):
    seen = set()
    for num in arr:
        complement = target-num
        if complement in seen:
            return complement,num
        seen.add(num)
    return None 