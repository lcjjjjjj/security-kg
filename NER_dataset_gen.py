import json

# read data.json file as utf-8 encoding
with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def generate_ner_dataset(data):
    save_data = []
    for item in data:
        try:
            save_item = {
                'sentence': item['cveId']+': '+item['sentence'],
                'entities': []
            }
            save_data.append(save_item)
        except KeyError:
            continue
    
    return save_data

if __name__ == '__main__':
    save_data = generate_ner_dataset(data)
    print(len(save_data))
    print(save_data[:5])
    # save save_data in file ner_dataset.json as utf-8 encoding
    with open('./ner_dataset.json', 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False)
