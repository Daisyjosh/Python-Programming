# To print N natural numbers in descending order.
def print_desc(n):
    if(n==0): # Base Case
        return
    print(n,end=" ") # Prints even before recursive call.
    print_desc(n-1) # Recursive call with smaller input
print_desc(5)