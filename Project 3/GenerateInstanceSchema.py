import json
import sys

def generate_instance_schema(schema_file):
    # Load the schema file
    with open(schema_file, 'r') as f:
        schema = json.load(f)

    # Generate the instance schema
    instance_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {}
    }

    for entity in schema["entities"]:
        entity_name = entity["name"]
        entity_properties = {}
        for attribute in entity["attributes"]:
            attribute_name = attribute["name"]
            attribute_type = attribute["type"]
            if attribute_type == "integer":
                entity_properties[attribute_name] = {"type": "integer"}
            elif attribute_type == "string":
                entity_properties[attribute_name] = {"type": "string", "maxLength": attribute["size"]}
        instance_schema["properties"][entity_name] = {"type": "array", "items": {"type": "object", "properties": entity_properties}, "minItems": 1}

    return json.dumps(instance_schema, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python GenerateInstanceSchema.py <schema_file>")
        sys.exit(1)

    schema_file = sys.argv[1]
    instance_schema = generate_instance_schema(schema_file)
    print(instance_schema)
