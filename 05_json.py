import json

data = {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}

with open('data_file.json', 'w') as write_file:
    # Dictionary to JSON FILE
    json.dump(data, write_file)

with open('data_file.json') as read_file:
    # Reads data from JSON FILE to dictionary
    read_data = json.load(read_file)

# Dictionary to JSON STRING
data_string = json.dumps(read_data)
print(data_string)
# JSON STRING to dictionary
loaded_dict = json.loads(data_string)
print(loaded_dict)