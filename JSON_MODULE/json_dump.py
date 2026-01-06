import json

# json.dump() is used to dump / store the python object to json file.
# dump is different from dumps.
# dumps is used for string handling.
# dump is used for file handling.

obj = {
    "name" : "Daisy",
    "College" : "SIET",
    "Departement" : "EEE"
}

with open("data.json","w") as f:
    json.dump(obj,f,indent=4,sort_keys=True) # Everything in the data.json file will be overwritten by obj.
    
    
# indent is used to provide indentation for the given input.
# sort_keys sort the keys. 
# Data is Overwritten.