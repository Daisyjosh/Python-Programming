# This "a+" operation is used to append text in the end of the file.

f = open("sample.txt","a+")
f.write("\n1234")
print(f.read()) #There's nothing to read after appending the text as it is last pointer in the file. 
f.close()