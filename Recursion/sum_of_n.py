# Sum of N natural Numbers.
def sum_n(n):
    if(n == 0): # Base Case.
        return 0
    return n + sum_n(n-1) # Recursive Case
print(sum_n(5))
