import json
import jsonschema
import sys
from jsonschema import validate, ValidationError

def validate_instance_file_generated(instance_file, schema_file):
    # load instance and schema files
    with open(instance_file) as f:
        instance_data = json.load(f)
    with open(schema_file) as f:
        schema_data = json.load(f)
    

    # validate instance file against schema
    try:
        validate(instance_data, schema_data)
        print("\nInstance File is Syntactically Correct\n")
    except ValidationError as e:
        print("\nSyntactic error in input file: {}\n".format(e))

    # validate entities
    print("\nSemantic Errors in instance file:\n")
    for entity_name, entities in instance_data['entities'].items():
        if entity_name not in schema_data['properties']:
            print(f"Error: entity {entity_name} not defined in schema")
            continue
        schema_entity = schema_data['properties'][entity_name]['items']['properties']
        for entity in entities:
            # check required fields
            for field in schema_entity:
                if field not in entity:
                    print(f"Error: missing required field {field} in {entity_name}")
            # check data types and range
            for field, value in entity.items():
                if field not in schema_entity:
                    continue
                field_type = schema_entity[field]['type']
                if field_type == 'integer':
                    if not isinstance(value, int):
                        print(f"Error: {field} in {entity_name} must be an integer")
                    else:
                        # check range
                        if 'minimum' in schema_entity[field]:
                            if value < schema_entity[field]['minimum']:
                                print(f"Error: {field} in {entity_name} must be >= {schema_entity[field]['minimum']}")
                        if 'maximum' in schema_entity[field]:
                            if value > schema_entity[field]['maximum']:
                                print(f"Error: {field} in {entity_name} must be <= {schema_entity[field]['maximum']}")
                elif field_type == 'string' and not isinstance(value, str):
                    print(f"Error: {field} in {entity_name} must be a string")
            # check for duplicate keys
            entity_keys = set(entity.keys())
            for other_entity in entities:
                if other_entity == entity:
                    continue
                other_keys = set(other_entity.keys())
                if entity_keys == other_keys:
                    if entity_keys.intersection(schema_entity) == entity_keys:
                        print(f"Error: {entity_name} with keys {entity_keys} is a duplicate")
            # check for invalid references
            if entity_name in instance_data['relationships']:
                for relationship_name, relationships in instance_data['relationships'][entity_name].items():
                    if relationship_name not in schema_data['relationships'][entity_name]:
                        print(f"Error: relationship {relationship_name} not defined in schema for {entity_name}")
                        continue
                    schema_relationship = schema_data['relationships'][entity_name][relationship_name]
                    for relationship in relationships:
                        for key, value in relationship.items():
                            if key not in schema_relationship:
                                print(f"Error: invalid field {key} in {relationship_name} relationship for {entity_name}")
                                continue
                            referenced_entity_name = schema_relationship[key]['refersTo']
                            if referenced_entity_name not in instance_data['entities']:
                                print(f"Error: referenced entity {referenced_entity_name} not defined in instance")
                                continue
                            referenced_entity_key = value
                            if referenced_entity_key not in [e.get(schema_relationship[key]['refersToKey']) for e in instance_data['entities'][referenced_entity_name]]:
                                print(f"Error: invalid reference {referenced_entity_key} in {relationship_name} relationship for {entity_name}")
                        
def validate_schema(schema_file_path):
    # Open and read the schema file
    with open(schema_file_path, 'r') as f:
        schema_data = json.load(f)

    # Validate syntax errors
    try:
        jsonschema.Draft7Validator.check_schema(schema_data)
    except jsonschema.exceptions.SchemaError as e:
        print(f"JSON syntax validation error: {e}")
        return False

    # Validate semantic errors
    entity_names = set()
    relationship_names = set()
    for entity in schema_data.get('entities', []):
        entity_name = entity.get('name')
        if not entity_name:
            print("Entity name not defined")
            return False
        if entity_name in entity_names:
            print(f"Duplicate entity name: {entity_name}")
            return False
        entity_names.add(entity_name)

        attribute_names = set()
        primary_key_names = set(entity.get('primaryKey', []))
        for attribute in entity.get('attributes', []):
            attribute_name = attribute.get('name')
            if not attribute_name:
                print(f"Attribute name not defined for entity {entity_name}")
                return False
            if attribute_name in attribute_names:
                print(f"Duplicate attribute name in entity {entity_name}: {attribute_name}")
                return False
            attribute_names.add(attribute_name)

            if attribute_name in primary_key_names:
                primary_key_names.remove(attribute_name)

        if primary_key_names:
            print(f"Key attribute not defined in entity {entity_name}: {primary_key_names}")
            return False

    for relationship in schema_data.get('relationships', []):
        relationship_name = relationship.get('name')
        if not relationship_name:
            print("Relationship name not defined")
            return False
        if relationship_name in relationship_names:
            print(f"Duplicate relationship name: {relationship_name}")
            return False
        relationship_names.add(relationship_name)

        entity_names = set()
        for entity in relationship.get('entities', []):
            entity_name = entity.get('name')
            if not entity_name:
                print("Entity name not defined in relationship")
                return False
            if entity_name in entity_names:
                print(f"Duplicate entity name in relationship {relationship_name}: {entity_name}")
                return False
            entity_names.add(entity_name)

            # Check if entity is defined in the schema
            if entity_name not in entity_names:
                print(f"Entity {entity_name} in relationship {relationship_name} not defined")
                return False

    return True


def validate_instance_file(instance_file, instance_schema):
    # Load the JSON files as dictionaries
    with open(instance_file, 'r') as f:
        instance_data = json.load(f)

    with open(instance_schema, 'r') as f:
        schema_data = json.load(f)

    # Check for syntax errors
    try:
        jsonschema.validate(instance_data, schema_data)
    except jsonschema.exceptions.ValidationError as e:
        print(f"JSON syntax validation error: {e}")
        
    # Check for semantic errors
    semantic_errors = []

    # Check for data type errors in entity and relationship instances
    for entity_name in instance_data:
        if entity_name in schema_data["entities"]:
            for instance in instance_data[entity_name]:
                for attr in instance:
                    if attr in schema_data["entities"][entity_name]["attributes"]:
                        if type(instance[attr]) != schema_data["entities"][entity_name]["attributes"][attr]["type"]:
                            semantic_errors.append(f"Data type error: {attr} in {entity_name} instance")
        elif entity_name in schema_data["relationships"]:
            for instance in instance_data[entity_name]:
                for attr in instance:
                    if attr in schema_data["relationships"][entity_name]["attributes"]:
                        if type(instance[attr]) != schema_data["relationships"][entity_name]["attributes"][attr]["type"]:
                            semantic_errors.append(f"Data type error: {attr} in {entity_name} instance")


    # Check for primary key errors in entity instances
    for entity_name in instance_data:
        if entity_name in schema_data["entities"]:
            for instance in instance_data[entity_name]:
                for pk_attr in schema_data["entities"][entity_name]["primary_key"]:
                    if pk_attr not in instance:
                        semantic_errors.append(f"Primary key error: {pk_attr} not in {entity_name} instance")

    # Check for cardinality errors in relationship instances
    for rel_name in instance_data:
        if rel_name in schema_data["relationships"]:
            for instance in instance_data[rel_name]:
                if instance["cardinality"] not in schema_data["relationships"][rel_name]["cardinality"]:
                    semantic_errors.append(f"Cardinality error: {instance['cardinality']} in {rel_name} instance")

    # Check for participation errors in relationship instances
    for rel_name in instance_data:
        if rel_name in schema_data["relationships"]:
            for instance in instance_data[rel_name]:
                if instance["participation"] not in schema_data["relationships"][rel_name]["participation"]:
                    semantic_errors.append(f"Participation error: {instance['participation']} in {rel_name} instance")

    # Check for invalid attributes in relationship instances
    for rel_name in instance_data:
        if rel_name in schema_data["relationships"]:
            for instance in instance_data[rel_name]:
                for attr in instance:
                    if attr not in schema_data["relationships"][rel_name]["attributes"]:
                        semantic_errors.append(f"Invalid attribute: {attr} in {rel_name} instance")

    if semantic_errors:
        return semantic_errors
    else:
        return None



def main():
    #validating generated instance schema
    print("\n---Validating Instance file against Generated Instance Schema---")
    validate_instance_file_generated(sys.argv[1], sys.argv[2])


    # validating DB SCHEMA
    print("\n\n---Validating DB Schema---\n")

    if validate_schema(sys.argv[3]):
        print('\nDB Schema Validation successful')
    else:
        print('\nDB Schema Validation failed')


    # Validating instance file against DB SCHEMA
    print("\n\n---Validating Instance file against DB Schema---")

    semantic_errors = validate_instance_file(sys.argv[1], sys.argv[3])

    if semantic_errors:
        print("\nSemantic errors in Instance File:")
        for error in semantic_errors:
            print(error)


    # If there are no errors, print a success message
    if not semantic_errors:
        print("\nInstance file is Successfully Validated Against DB Schema")

if __name__ == "__main__":
    main()
