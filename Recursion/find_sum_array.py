def sum_arr(arr,n,i):
    if(i == n):
        return 0
    return arr[i] + sum_arr(arr,n,i+1)
arr = [1,2,3,4,5]
print(sum_arr(arr,5,0))

