import json
import os

# Step 1: Create a Python dictionary
data = {
    "name": "Jose Doe",
    "age": 33,
    "is_student": False,
    "courses": ["Web Design", "GLSL", "Dart"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "BC",
        "zip_code": "12345"
    }
}

# Define the output directory and file path
output_dir = "output"
output_file = os.path.join(output_dir, "data.json")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# # # Step 3: Write JSON to a file
# with open(output_file, "w") as json_file:
#     json.dump(data, json_file, indent=3)

# print("\nJSON data has been written to data.json")

# Step 4: Read JSON from a file
with open(output_file, "r") as json_file:
    data_from_file = json.load(json_file)

print("\nData read from data.json:")
print(data_from_file)