# use python numpy and sklearn package to devide a dataset in train, test and dev as save as json files
from sklearn.model_selection import train_test_split
import json

# open ner_data.json and read the data as utf-8 encoding
with open('ner_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

train, test = train_test_split(data, test_size=0.2, random_state=42)
test, dev = train_test_split(test, test_size=0.5, random_state=42)

print(len(train))
print(len(test))
print(len(dev))

# save train, test, dev as json file with utf-8 encoding
with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(train, f, ensure_ascii=False)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(test, f, ensure_ascii=False)

with open('dev.json', 'w', encoding='utf-8') as f:
    json.dump(dev, f, ensure_ascii=False)
