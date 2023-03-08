import json
import sys

def generate_instance_schema(schema_file):
    with open(schema_file) as f:
        schema_data = json.load(f)

    instance_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {}
    }



    for entity in schema_data["entities"]:
        entity_name = entity["name"]
        entity_properties = {}

        for attribute in entity["attributes"]:
            attribute_name = attribute["name"]
            attribute_type = get_attribute_type(attribute["type"])
            attribute_length = attribute["size"]
            entity_properties[attribute_name] = {"type": attribute_type}
            if attribute_length is not None:
                entity_properties[attribute_name]["maxLength"] = attribute_length

        instance_schema["properties"][entity_name] = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": entity_properties,
                "required": [attr["name"] for attr in entity["attributes"]]
            }
        }

    for relationship in schema_data["relationships"]:
        relationship_name = relationship["name"]
        relationship_properties = {}

        for attribute in relationship["attributes"]:
            attribute_name = attribute["name"]
            attribute_type = get_attribute_type(attribute["type"])
            attribute_length = attribute["size"]
            relationship_properties[attribute_name] = {"type": attribute_type}
            if attribute_length is not None:
                relationship_properties[attribute_name]["maxLength"] = attribute_length

        for entity in relationship["entities"]:
            entity_name = entity["name"]
            if entity["participation"] == "mandatory":
                if entity_name not in instance_schema["properties"]:
                    instance_schema["properties"][entity_name] = {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                instance_schema["properties"][entity_name]["items"]["properties"][relationship_name] = {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": relationship_properties,
                        "required": [attr["name"] for attr in relationship["attributes"]]
                    },
                    "minItems": 1
                }
            elif entity["participation"] == "optional":
                if entity_name not in instance_schema["properties"]:
                    instance_schema["properties"][entity_name] = {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                instance_schema["properties"][entity_name]["items"]["properties"][relationship_name] = {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": relationship_properties,
                        "required": [attr["name"] for attr in relationship["attributes"]]
                    }
                }

    instance_schema = json.dumps(instance_schema, indent=2)
    with open("GeneratedInstanceSchema.json", "w") as f:
        f.write(instance_schema)
        print(instance_schema)
        print("Generated instance schema file: GeneratedInstanceSchema.json")

def get_attribute_type(attribute_type):
    if attribute_type == "integer":
        return "integer"
    elif attribute_type == "string":
        return "string"
    elif attribute_type == "float":
        return "number"
    elif attribute_type == "boolean":
        return "boolean"
    else:
        return "string"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python GenerateInstanceSchema.py <schema_file>")
    else:
        generate_instance_schema(sys.argv[1])
