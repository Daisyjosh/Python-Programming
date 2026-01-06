n = int(input("Enter n: "))
nums = [-2,-4,3,5,2,-1]

# Expected Output: [0,0,3,5,2,0]

result = [0 if val < 0 else val for val in nums]

print(result)