import json

with open('C:\\Users\\Mike\\Documents\\BakalarskaPraca\\generalized-log-decoder-copy\\windows-log-radka.json') as json_file:
    json1 = json.load(json_file)


with open('C:\\Users\\Mike\\Documents\\BakalarskaPraca\\generalized-log-decoder-copy\\windows-log-regina.json') as json_file:
    json2 = json.load(json_file)

# print("json1:", json1)
# print("json2:", json2)

# def json_compare(json1, json2):
#     #Compare all keys
#     for key in json1.keys():
#         #if key exist in json2:
#         if key in json2.keys():
#             #If subjson
#             if type(json1[key]) == dict:
#                 json_compare(json1[key], json2[key])
#         else:
#             return False
#     return True


# print(json_compare(json1, json2))

def compare(json1, json2):
    if set(json1.keys()) == set(json2.keys()):
        print("Works")
    else:
        print("Does not work")

compare(json1, json2)

# data = {"test": "test"}

# with open('exported/data.json', 'w') as f:
#     json.dump(data, f, indent=4, separators=(',', ': '))