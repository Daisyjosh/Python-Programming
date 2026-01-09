# Printing N natural Numbers in Ascending Order.
def print_asc(n):
    if(n == 0): # Base Case
        return 
    print_asc(n-1) # Recursive Call before printing
    print(n,end=" ") # Prints while the function is returning from recursive calls.
print_asc(5)