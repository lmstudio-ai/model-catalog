"""
A script to create a catalog.json file from the JSON files in the models folder.
"""
import os
import subprocess
import json

# Get the python path from an env variable or fallback to `python`:
python = os.environ.get('PYTHON', 'python')

# Get all JSON files from the models folder
json_files = [f for f in os.listdir('models') if f.endswith('.json')]

# Initialize an empty list to store the JSON objects
json_objs = []

# Run validate.py for each JSON file
for json_file in json_files:
    result = subprocess.run([python, 'validate.py', 'schema.json', f'models/{json_file}'], capture_output=True)
    if result.returncode != 0:
        print(f"Validation failed for {json_file}. Ret code: {result.returncode}")
        exit(1)
    else:
        with open(f'models/{json_file}', 'r') as f:
            json_obj = json.load(f)
            json_objs.append(json_obj)

# Write the JSON objects to catalog.json
with open('catalog.json', 'w') as f:
    json.dump(json_objs, f, indent=4)

# Run validate.py for catalog.json
result = subprocess.run([python, 'validate.py', 'schema.json', 'catalog.json'], capture_output=True)
if result.returncode != 0:
    print("Validation failed for catalog.json")
    exit(1)
