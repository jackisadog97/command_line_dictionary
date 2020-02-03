import json

data = json.load(open("data_file.json","r"))
print(type(data))
print(data["data"])