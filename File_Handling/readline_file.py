# Reading a file line by line. 
# View the sample code before executing(for better understanding).
# Reads the file character by character also the invisible new line tag.
f = open("sample.txt","r")

data = f.readline()
print(data)

f.close()