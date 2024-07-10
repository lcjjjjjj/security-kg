import os
import json

def get_cve_info(cve_file):
    with open(cve_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return_data = {}
    # print(data.keys())
    # get json values cveMetadata and containers
    # print(data['cveMetadata']['cveId'])
    # print(data['containers']['cna']['descriptions'])
    return_data['cveId'] = data['cveMetadata']['cveId']
    for description in data['containers']['cna']['descriptions']:
        if description['lang'] == 'en' or description['lang'] == 'eng':
            return_data['sentence'] = description['value']
    # print(return_data)
    return return_data

def cve_info_extraction():
    save_data = []
    for year in os.listdir('./cves'):
        for number in os.listdir(os.path.join('./cves', year)):
            for item in os.listdir(os.path.join('./cves', year, number)):
                try:
                    save_data.append(get_cve_info(cve_file=os.path.join('./cves', year, number, item)))
                except KeyError:
                    continue
    return save_data

if __name__ == '__main__':
    # get_cve_info(cve_file='./cves/2015/0xxx/CVE-2015-0941.json')
    save_data = cve_info_extraction()
    print(len(save_data))
    print(save_data[:3])
    # save save_data in a json file named data.json as utf-8 encoding
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False)