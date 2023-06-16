"""
A simple script to validate a JSON file against a JSON schema.
Usage: python validate.py <schema_file> <json_file>
"""
import json
from jsonschema import validate, ValidationError
import sys

def validate_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        print("JSON file is valid.")
        sys.exit(0)
    except ValidationError as v:
        print("JSON file is invalid.")
        print(v)
        sys.exit(42)

def main(schema_file, json_file):
    with open(schema_file, 'r') as f:
        schema = json.load(f)

    with open(json_file, 'r') as f:
        json_data = json.load(f)
        if not isinstance(json_data, list):
            json_data = [json_data]

    return validate_json(json_data, schema)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate.py <schema_file> <json_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])