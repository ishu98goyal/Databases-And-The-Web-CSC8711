CSc 8711 Databases and the Web - Spring 2023 - Programming Project 1

Csc 8711, Databases and the Web - Programming Project 1
=======================================================

To be completed in teams of 2 members, with one person focusing on frontend and the other focusing on backend. This does not preclude helping each other!

### A Generic Multi-Dimensional Database Search Engine (MDB)

In this programming assignment, you will implement a Web-based search engine that provides searching capabilities on any multi-dimensional data resource such as colleges, automobiles, etc. The Web application should be generic in the sense that it should work on data coming from different domains describing entities in the respective domains. The following database schema files are provided:

*   [dbSchema.sql](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/files/dbSchema.sql.txt)
*   [collegeMetaData.sql](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/files/collegeMetaData.sql.txt)
*   [collegeData.sql](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/files/collegeData.sql.txt)
*   [autoMetaData.sql](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/files/autoMetaData.sql.txt)
*   [autoData.sql](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/files/autoData.sql.txt)

dbSchema.sql contains definitions of tables that hold generic information about the domains and the properties that describe entities in domains. This file also contains tables that hold information about users and their bookmarks.

For each domain, there are two sql files: (1) one containing meta data related to the properties and the definition of the "fact" table that records information about the entities in that domain, and (2) the other containing data about the entities.

### Technologies to be used

You will implement this project as a Single Page Application (SPA) using modern Web application architecture with:

1.  MySQL database
2.  Backend Web Services using GraphQL in Python Graphene
3.  Frontend with HTML/Javascript or ReactJS or AngularJS

### User Interface

Here are the screenshots of the user interface, shown progressively as the user interacts with the UI:

#### Initial Screen

![](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/mdb1.png)

#### Screen after user chooses a domain of interest

![](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/mdb2.png)

#### Screen after user enters userid

![](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/mdb3.png)

#### Screen after user chooses values for some properties and submits the search.

Before submitting the search, the user bookmarked the search and had deleted one of the previous bookmarks! ![](https://tinman.cs.gsu.edu/~raj/8711/sp23/p1/mdb8.png)

#### Notes and requirements

1.  The Web application should be a Single Page Application (SPA). The UI should be divided into four different parts:
    *   Choose domain and userid input section
    *   Search criteria section (displaying 3 or 4 properties at a time), and have the ability to go next/previous for additional properties, reset search criteria, as well as ability to bookmark a particular search.
    *   Bookmarks display and delete section. The bookmarks themselves should be clickable and upong click the search properties should be populated with values in the bookmark.
    *   Results section
2.  The next and previous operations to display additional properties should take care of the edge cases: last page and first page; in these cases the next (or previous) options should be disabled accordingly.
3.  A user is allowed a maximum of 5 bookmarks; As soon as the user saves the fifth bookmark for a particular domin, the add bookmark option should be disabled and as soon as a bookmark is deleted the option should be re-enabled. A unique bookmark name is required to add a new bookmark.
4.  After you switch domains, userid and bookmarks sections should be reset.

#### What to Submit?

1.  All code to develop the project, arranged in 3 directories: db, frontend, backend.
2.  Short project report and contributions of group members. (1-2 pages in pdf)