import json

with open(r"data\birds.json", 'r') as birds:
    data = json.load(birds)
    print(data[1])