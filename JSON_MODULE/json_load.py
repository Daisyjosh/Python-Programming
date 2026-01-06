import json

# json.load() is used to load json file to python object.
# load is different from loads.
# loads is used for string handling.
# load is used for file handling.

with open("data.json","r") as f: # Readin a File
    py_obj = json.load(f) # Loading a json file to python object
    print(type(py_obj))
    print(py_obj)

    # file closes automatically.

