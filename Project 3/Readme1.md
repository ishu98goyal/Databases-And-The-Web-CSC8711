
Part I: JSON Schema for Schema Files
================

StudentDB Schema
--------

This JSON schema describes the structure of a database for storing information about students and their relationships to other entities.

Entities
--------

The `entities` property is an array of objects, each of which represents an entity in the database. Each entity object has a `name` property and an `attributes` property, which is an array of objects representing the attributes of the entity. The `primaryKey` property is an array of strings, specifying the primary key of the entity.

Relationships
-------------

The `relationships` property is an array of objects, each of which represents a relationship between entities in the database. Each relationship object has a `name` property and an `entities` property, which is an array of objects representing the entities in the relationship. The `attributes` property is an array of objects representing the attributes of the relationship. 
 


Part II: Python program to Generate JSON Schema for Instance Files
================================

This Python script generates a JSON instance schema based on an input schema file in JSON format.

Usage
-----

To run the script, use the following command in your terminal or command prompt:

    python GenerateInstanceSchema.py <schema_file>

Replace `<schema_file>` with the path to your schema file.

The script will generate a JSON instance schema file named `GeneratedInstanceSchema.json` in the same directory as the script.

Functionality
-------------

The script reads the input schema file and extracts information about entities and their attributes, as well as relationships and their attributes. It then generates a JSON instance schema that includes the type and properties for each entity and relationship, as well as required attributes.

Entities with mandatory participation in a relationship are required to have at least one instance of that relationship. Optional participation in a relationship does not have this requirement.




Part III: Validate Instance Files
==============================

This program contains three functions that validate a given JSON schema and instance file. The functions are:

validate\_instance\_file\_generated
-----------------------------------

This function loads the instance and schema files and validates the instance file against the Instance generated schema (part II). It then checks for semantic errors in the instance file, including missing required fields, incorrect data types and range, duplicate keys, and invalid references.

### Inputs

*   `instance_file`: The path to the instance file to be validated.
*   `schema_file`: The path to the schema file against which the instance file is to be validated.

### List of errors the function is checking

*   Syntax error in the input file
*   Missing required fields
*   Incorrect data types and range
*   Duplicate keys
*   Invalid references

validate\_schema
----------------

This function validates the given schema file for syntax and semantic errors. It checks for duplicate entity and relationship names, missing entity and attribute names, and missing primary key attributes.

### Inputs

*   `schema_file_path`: The path to the schema file to be validated.

### List of errors the function is checking

*   JSON syntax validation error
*   Duplicate entity and relationship names
*   Missing entity and attribute names
*   Missing primary key attributes

validate\_instance\_file
------------------------

This function loads the instance and schema files and validates the instance file against the DB schema.

### Inputs

*   `instance_file`: The path to the instance file to be validated.
*   `schema_file`: The path to the DB schema file against which the instance file is to be validated.

### List of errors the function is checking

*   Syntax error in the input file
*   Missing required fields
*   Incorrect data types and range
*   Duplicate keys
*   Invalid references

Usage
-----

    python Validate.py <instance_file> <generated_instance_schema_file> <db_schema_file>


Example: 

    python Validate.py StudentDBInstance.json GeneratedInstanceSchema.json StudentDBSchema.json



Part IV: Generate Relational Design
===========================

This script generates SQL statements to create tables in a relational database based on a JSON schema file and outputs to the terminal. The script takes one argument: the path to the JSON schema file.

Usage
-----

    python GenerateRelationalDesign.py <schema_file>

Replace <schema\_file> with the path to your JSON schema file.

Dependencies
------------
Python Modules:
*   JSON
*   SYS

JSON Schema
-----------

The JSON schema should have two top-level keys: `entities` and `relationships`. The `entities` key should map to a list of objects representing entities in the database. Each entity object should have the following keys:

*   `name`: the name of the entity
*   `primaryKey`: an array of one or more attribute names that make up the primary key of the entity
*   `attributes`: a list of objects representing the attributes of the entity. Each attribute object should have the following keys:

*   `name`: the name of the attribute
*   `type`: the data type of the attribute. Currently supported types are `integer` and `string`
*   `size`: the size of the attribute. Required for `string` attributes, ignored for `integer` attributes.

The `relationships` key should map to a list of objects representing relationships between entities. Each relationship object should have the following keys:

*   `name`: the name of the relationship
*   `entities`: an array of two objects representing the entities involved in the relationship. Each entity object should have the following keys:

*   `name`: the name of the entity
*   `cardinality`: the cardinality of the relationship. Currently supported values are `one` and `many`

