# Print whether the word exist or not in the file.
# If present print the nth line that it is present.
data = True
line = 1
target = "python"
with open("file_for_practice.txt","r") as f:
    while data:
        data = f.readline()
        if(target in data):
            print("Word found!!")
            print(f"{target} found at line {line}")
            break
        line += 1
        
    