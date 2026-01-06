n = int(input("Enter n: "))
square = [i*i for i in range(n) if i % 2 != 0]
print(square)