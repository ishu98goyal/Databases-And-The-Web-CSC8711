Usage
-----

Run the script using `python BOM.py "USERNAME" "PASSWORD"` command in the terminal or command prompt.

The program will display a menu with the following options:

*   `(c) cost of part`: Calculates the cost of a part.
*   `(s) sub-parts`: Displays the subparts of a part and their quantities.
*   `(q) quit`: Exits the program.

When you choose `(c) cost of part` or `(s) sub-parts`, the program will prompt you to enter the name of the part for which you want to compute the cost or subparts respectively.

The program will then use the Py2Neo library to query the Neo4j database and compute the cost or subparts.