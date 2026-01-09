def IsSorted(arr,n,i):
    if(i == n-1):
        return True
    if(arr[i] > arr[i+1]):
        return False
    return IsSorted(arr,n,i+1)
print(IsSorted([1,2,3,4,5],5,0))