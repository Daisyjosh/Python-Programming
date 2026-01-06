# Opening a file with WITH keyword.
# Automatically closes when the operations are done.

with open("sample.txt","r") as f: 
    print(f.read())

    # No need to explicitily close the file.