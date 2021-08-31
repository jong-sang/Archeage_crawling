import json

with open('channelData.json') as json_file:
    json_data = json.load(json_file)
    
a = json_data
b = a["다후타"]["cocodor"]
print(type(b))
print(b)
