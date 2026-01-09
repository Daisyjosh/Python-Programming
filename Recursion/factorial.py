# To find the factorial of Number N.
def factorial(n):
    if(n==0): # Base Case factorial of 0 is 1.
        return 1
    return n * factorial(n-1) # Recursive case: reduces problem size.
print(factorial(5))
