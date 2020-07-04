# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.


import json
# help(json)
dict = {'name': "Asmita", 'age': 21}

with open('asmita.json', 'w') as fb:
    json.dump(dict, fb)

fb = open('asmita.json', 'r')
print(fb.read())
print(type(fb.read()))