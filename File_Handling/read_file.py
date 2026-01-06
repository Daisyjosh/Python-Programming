# Read a file
f = open("sample.txt","r") # Return file object
data = f.read() # Reads the data
print(data) # Prints the Data 
print(type(data)) # Type of Data

f.close()