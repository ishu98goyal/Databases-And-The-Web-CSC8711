 CSc 8711 Databases and the Web - Spring 2023 - Project 6

### Csc 8711, Databases and the Web - Project 6

**Due**: Wednesday, April 26th (STRICT DEADLINE)  

This program will constitute 25% of your final exam. The other 75% will be from a take home problem set given to you on April 21th. All programs and problems for the final exam are due April 26th by Midnight - STRICT DEADLINE!!!

### Neo4J Graph Database

#### BILL OF MATERIALS

Consider the Neo4J database loaded in [loadParts.py](loadParts.py). Run this program to create the graph database. Then, write a program to compute cost of parts as well as basic subparts of parts. A sample run is given below:

macbook-pro:bom raj$ python3 BOM.py raj 1raj23

(c) cost of part
(s) sub-parts
(q) quit

What do you want to see: c
Enter part name: engine
Cost of engine is 744.0

(c) cost of part
(s) sub-parts
(q) quit

What do you want to see: c
Enter part name: cylinder
Cost of cylinder is 29.0

(c) cost of part
(s) sub-parts
(q) quit

What do you want to see: s
Enter part name: engine
Subparts of pname: 

bolt 192
screw 136
gasket 16
sparkplug 4


(c) cost of part
(s) sub-parts
(q) quit

What do you want to see: s
Enter part name: cylinder
Subparts of pname: 

bolt 4
screw 6
gasket 3


(c) cost of part
(s) sub-parts
(q) quit

What do you want to see: q
macbook-pro:bom raj$

Note: loadData.py is an example of a program that creates one instance of the database; Your solution should work on any other graph data set that could be loaded by a similar program; i.e. the Node and Relationship types will be the same, but instances of Nodes and Relationships may be different.