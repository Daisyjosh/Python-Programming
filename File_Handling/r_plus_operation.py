# Using r+ operation in file Handling.
# We can Read the file and write in the file.
# The pointer Begins from the starting character in the file.

# Preview the read file before running the program for better understanding.

f = open("sample.txt","r+")

f.write("1234") # Overwrites only the first three characters of the file.
print(f.read()) # Reads the entire file after the overwritten value to the last one.

f.close()