import json

class Converter:
    @classmethod
    def json_to_dict(cls, json_str):
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            print("Error decoding JSON string.")
            return None


json_string = '{"name": "reza", "age": 26, "city": "kermanshah"}'
parsed_dict = Converter.json_to_dict(json_string)
if parsed_dict:
    print("Parsed dictionary:")
    for key, value in parsed_dict.items():
        print(f"{key}: {value}")
else:
    print("Failed to parse the JSON string.")
