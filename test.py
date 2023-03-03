import json
import os

# with open('C:\\Users\\Mike\\Documents\\BakalarskaPraca\\generalized-log-decoder-copy\\windows-log-radka.json') as json_file:
#     json1 = json.load(json_file)


# with open('C:\\Users\\Mike\\Documents\\BakalarskaPraca\\generalized-log-decoder-copy\\windows-log-regina.json') as json_file:
#     json2 = json.load(json_file)

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
        return True
    else:
        return False

#compare(json1, json2)

def numOfFiles():
    count = 0
    dir_path = f'exported\\other'
    for path in os.scandir(dir_path):
        if path.is_file():
            count += 1
    print('file count:', count)


def cycleFiles():
    count = 0
    dir_path = f'exported\\other'
    for path in os.scandir(dir_path):
        if path.is_file():
            count += 1
    
    data = {
         "vyskusame": "test"
    }
    
    similar = 0
    
    for i in range(count):
        with open(f'exported\\other\\other{i+1}_batch_1.json') as json_file:
            json1 = json.load(json_file)
            json2 = data
            if compare(json1, json2) == True:
                        similar += 1
                        print("Same file")
            elif compare(json1, json2) == False:
                        print("Different file")
            # for f in range(count):
            #     with open(f'exported\\other\\other{f+1}_batch_1.json') as json_file:
            #         json2 = json.load(json_file)
    print(similar)
                    
                
cycleFiles()
# data = {"test": "test"}

# with open('exported/data.json', 'w') as f:
#     json.dump(data, f, indent=4, separators=(',', ': '))