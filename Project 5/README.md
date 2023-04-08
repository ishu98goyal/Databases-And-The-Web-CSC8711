 CSc 8711 Databases and the Web - Spring 2023 - Project 5

### Csc 8711, Databases and the Web - Project 5

**Due**: Wednesday, April 19th  
Pair Assignment (Maximum of 2 persons per group).

### Semantic Web, RDF, SPARQL, Web Services, UI

Consider the Nobel Ontology specified in the following OWL files:

*   [nobel.owl](data/nobel.owl)
*   [nobeldata.owl](data/nobeldata.owl)

Build a Web application that allows the user to browse the data in this ontology.

#### Project Requirements

1.  Use Python-SPARQL API to run SPARQL queries against the Ontologies and embed these into Python-Flask RESTful Services. Some of the endpoints you would need are (add other end points as needed):
    
    /nobel/nations
    GET: Return sorted names of all nations
    
    /nobel/categories
    GET: Return sorted names of all nobel categories
    
    /nobel/years
    GET: Return sorted years nobels are awarded
    
    /nobel/<year>
    GET: Return list of all nobel winners for the given year
    
    /nobel/nations/<nation>
    GET: Return list of all nobel winners for the given nation
    
    /nobel/categories/<category>
    GET: Return list of all nobel winners for the given category
    
    /nobel/<year>/<category>
    GET: Return list of all nobel winners for the given year and category
    
2.  Build Web Client/UI to enable users to browse the Nobel Winners by Nation, Year, and Category. The project will be graded for a reasonable UI.
3.  You should build a separate page giving all details for individual winners (e.g. a separate Web page for winner of the Physics Prize in 2010, etc).