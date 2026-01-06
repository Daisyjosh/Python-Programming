import json

# json.loads() is used to load the json string into python objects.
# loads is different from load
# loads => load strings

json_Str = '{"name":"Daisy panimariyal","isStudent": true,"Fear":null}' # These are json values 

py_obj = json.loads(json_Str) # Now loaded as python objects 

# In json => true, null
# In python => True, None
# See the Transision
print(type(json_Str))
print("After loads....")
print(type(py_obj),py_obj)
