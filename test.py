import json

# read data.json file as utf-8 encoding
with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(len(data))

# print the first 5 records
print(data[:5])