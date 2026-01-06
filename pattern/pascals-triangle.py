from math import factorial
rows = 5
for n in range(rows):
    for space in range(1,rows-n):
        print(end=" ")
    for r in range(n+1):
        ncr = factorial(i) // (factorial(r)*factorial(n-r))
        print(ncr,end=" ")
    print()

