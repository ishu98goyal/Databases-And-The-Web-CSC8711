#Project 5 - Nobel Ontology Project

## Team Members:
1. Pooja Baba: Frontend
2. Ishu Goyal: Backend

API Documentation
=================

This API provides information about Nobel Prize winners. It uses an RDF graph stored in two OWL files to retrieve and return data about the winners, including their names, nationalities, and the categories and years in which they won.

Endpoints
---------

The following endpoints are available:

*   `/nobel/nations` (GET): Returns a sorted list of all nations.
*   `/nobel/categories` (GET): Returns a sorted list of all Nobel categories.
*   `/nobel/years` (GET): Returns a sorted list of all years Nobel Prizes were awarded.
*   `/nobel/<year>` (GET): Returns a list of all Nobel winners for the given year.
*   `/nobel/nations/<nation>` (GET): Returns a list of all Nobel winners for the given nation.
*   `/nobel/categories/<category>` (GET): Returns a list of all Nobel winners for the given category.

Execution
---------

The application is written in Python using the Flask framework, and uses the rdflib library to parse the OWL files. 
Command To execute the backend:

    python backend.py