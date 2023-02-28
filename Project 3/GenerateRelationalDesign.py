import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: GenerateRelationalDesign.py <schema_file>")
        return
    
    schema_file = sys.argv[1]
    
    with open(schema_file) as f:
        schema = json.load(f)
    
    for entity in schema["entities"]:
        table_name = entity["name"]
        primary_key = entity["primaryKey"][0]
        attributes = []
        
        for attribute in entity["attributes"]:
            attr_name = attribute["name"]
            attr_type = get_sql_type(attribute["type"], attribute["size"])
            attributes.append((attr_name, attr_type))
        
        sql = f"CREATE TABLE {table_name} (\n"
        sql += f"    {primary_key} INT NOT NULL,\n"
        
        for attr_name, attr_type in attributes:
            if attr_name != primary_key:
                sql += f"    {attr_name} {attr_type},\n"
        
        sql += f"    PRIMARY KEY ({primary_key})\n"
        sql += ");\n"
        
        print(sql)
    
    for relationship in schema["relationships"]:
        left_entity = relationship["entities"][0]["name"]
        right_entity = relationship["entities"][1]["name"]
        relationship_name = relationship["name"]
        
        if relationship["entities"][0]["cardinality"] == "one":
            left_cardinality = "1"
            right_cardinality = "n"
        else:
            left_cardinality = "n"
            right_cardinality = "1"
        
        sql = f"CREATE TABLE {left_entity}_{right_entity} (\n"
        sql += f"    {left_entity}_id INT NOT NULL,\n"
        sql += f"    {right_entity}_id INT NOT NULL,\n"
        sql += f"    PRIMARY KEY ({left_entity}_id, {right_entity}_id),\n"
        sql += f"    FOREIGN KEY ({left_entity}_id) REFERENCES {left_entity}(id),\n"
        sql += f"    FOREIGN KEY ({right_entity}_id) REFERENCES {right_entity}(id)\n"
        sql += ");\n"
        
        print(sql)

def get_sql_type(data_type, size):
    if data_type == "integer":
        return "INT"
    elif data_type == "string":
        return f"VARCHAR({size})"
    else:
        raise ValueError(f"Invalid data type: {data_type}")

if __name__ == "__main__":
    main()
