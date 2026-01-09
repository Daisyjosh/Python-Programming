def max_arr(arr,i):
    if i == (len(arr) - 1):
        return arr[i]
    maxi = max_arr(arr,i+1)
    if arr[i] > maxi:
        return arr[i]
    else:
        return maxi
print(max_arr([1,2,3,4,5],0))

    
    