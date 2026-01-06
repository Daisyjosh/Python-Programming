import json

# json.dumps() is used to store the python objects into json strings.
# dumps is different from dump
# dumps => dump string

#creating python dictionary..
py_obj = {
    "name" : "Daisy Panimariyal",
    "isStudent" : True,
    "Fear" : None
}
print(type(py_obj))

json_str = json.dumps(py_obj)

print("After dumps..")
print(type(json_str),json_str)