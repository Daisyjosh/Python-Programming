def fib(n):
    if(n == 0 or n == 1): # Base Case
        return n
    return fib(n-1) + fib(n-2)
    # For Example fib(5) = fib(4) + fib(3) => 5 = 3+2
print(fib(5))