import requests
import json

URL_FILE_NAME = 'opm.txt'
ALL_UNIT_FILE_NAME = 'all_units.txt'
UNIQUE_UNIT_FILE_NAME = 'unique_units.json'

def get_json_urls_from_file(filename):
    json_urls = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.endswith('.json'):
                    json_urls.append(line)
    except FileNotFoundError:
        print(f"Can not find file: '{filename}'")
    except Exception as e:
        print(f"wrong: {e}")

    return json_urls

def fetch_and_parse_json(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def extract_fields_with_units(data, url):
    try:
        from_name = url
        one_file_units = []
        
        resources = data.get('resources', [])
        if not resources:
            return
        
        fields = resources[0].get('schema', {}).get('fields', [])
        
        for resource in resources:
            fields = resource.get('schema', {}).get('fields', [])
            for field in fields:
                unit = field.get('unit')
                if unit:
                    unit_data = {
                        'unit': unit,
                        'name': field.get('name', 'unknown'),
                        'type': field.get('type', 'unknown'),
                        'from': from_name
                    }
                    one_file_units.append(unit_data)
        
        with open(ALL_UNIT_FILE_NAME, 'a', encoding='utf-8') as file:
            for item in one_file_units:
                unit_info = json.dumps(item, ensure_ascii=False)
                file.write(f"{unit_info},\n")


    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def remove_duplicates():
    with open(ALL_UNIT_FILE_NAME, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.strip()
        json_content = f'[{content[:-1]}]'
        data =  json.loads(json_content)

        seen = set()
        unique_data = []
        for item in data:
            identifier = (item['unit'], item['type'])
            if identifier not in seen:
                seen.add(identifier)
                unique_data.append(item)
        with open(UNIQUE_UNIT_FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(unique_data, file, ensure_ascii=False, indent=2)
        return unique_data



# step1 get all url
json_urls = get_json_urls_from_file(URL_FILE_NAME)

 # step2 parse filed
count = 0
for url in json_urls:
  print(f'start file: {count}/n')
  count += 1
  data = fetch_and_parse_json(url)
  extract_fields_with_units(data, url)

# step3 unique units
unique_units = remove_duplicates()

print('success get unique units')

