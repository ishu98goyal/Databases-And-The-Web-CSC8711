from flask import Flask, render_template, request
import rdflib
from flask import jsonify


g = rdflib.Graph()
g.parse("data/nobel.owl")
g.parse("data/nobeldata.owl")
print("graph has %s statements." % len(g))

app = Flask(__name__)

#/nobel/nations
#GET: Return sorted names of all nations
@app.route("/nobel/nations")
def nations():
    qres = g.query(
            """
            PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
            PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
            SELECT ?n
            {
                    ?g rdf:type table:PersonWinner;
                    table:nationality ?n.
                    }
            GROUP BY ?n
            ORDER BY ?n""")

    nation = []
    for row in qres:
        name = ("%s" % row).rsplit('/',1)[-1]
        nation.append(name)

    return jsonify(nation)

#/nobel/categories
#GET: Return sorted names of all nobel categories
@app.route("/nobel/categories")
def categories():
    qres = g.query(
            """
            PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
            PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
            SELECT ?w
            {
                    ?g rdf:type table:PersonWinner;
                    table:WonPrize ?w.
                    }
            GROUP BY ?w
            ORDER BY ?w""")

    unique_category = []
    for row in qres:
        category = ("%s" % row).split('/')[-4]
        if category not in unique_category:
            unique_category.append(category)

    return jsonify(unique_category)

#/nobel/years
#GET: Return sorted years nobels are awarded
@app.route("/nobel/years")
def year():
    qres = g.query(
            """
            PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
            PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
            SELECT ?w
            {
                    ?g rdf:type table:PersonWinner;
                    table:WonPrize ?w.
                    }
            GROUP BY ?w
            ORDER BY ?w""")

    unique_year = []

    for row in qres:
        year = ("%s" % row).split('/')[-2]
        if year not in unique_year:
            unique_year.append(year)

    unique_year.sort()

    return jsonify(unique_year)


#/nobel/<year>
#GET: Return list of all nobel winners for the given year
@app.route("/nobel/<int:year>", methods=['GET'])
def getYear(year):
    qres = g.query(
        """
        PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT ?n
        {
        ?g rdf:type table:PersonWinner;
        table:name ?n;
        table:WonPrize ?w.
        ?w table:yearWon ?y.
        FILTER (?y = """ + str(year) + """)
        }""")

    winners = []
    for row in qres:
        winners.append("%s" % row)

    winners.sort()
    return jsonify(winners)


#/nobel/nations/<nation>
#GET: Return list of all nobel winners for the given nation
@app.route("/nobel/nations/<string:nation>", methods=['GET'])
def getNation(nation):
#GET: Return list of all nobel winners for the given nation
    if nation[0].islower():
        nation = nation.capitalize()
    qres = g.query(
        """
        PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT ?n ?d
        {
            ?g rdf:type table:PersonWinner;
            table:name ?n;
            table:nationality ?d.
        }""")

    winners = []
    for row in qres:
        if nation in ("%s %s" % row):
            winners.append(("%s %s" % row).split("http",1)[0])

    return jsonify(winners)

#/nobel/categories/<category>
#GET: Return list of all nobel winners for the given category
@app.route("/nobel/categories/<string:category>", methods=['GET'])
def getCategory(category):
#GET: Return list of all nobel winners for the given nation
    qres = g.query(
        """
        PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT ?n ?w
        {
            ?g rdf:type table:PersonWinner;
            table:name ?n;
            table:WonPrize ?w.
        }
        GROUP BY ?w
        ORDER BY ?w""")


    winners = []
    for row in qres:
        if category in ("%s %s" % row):
            winners.append(("%s %s" % row).split("http", 1)[0])
    winners.sort()
    return jsonify(winners)

#/nobel/<year>/<category>
#GET: Return list of all nobel winners for the given year and category
@app.route("/nobel/<int:year>/<string:category>", methods=['GET'])
def getYearCategory(year, category):
    # Return list of all nobel winners for the given year and category
    qres = g.query(
        """
        PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT ?n ?w ?y
        {
            ?g rdf:type table:PersonWinner;
            table:name ?n;
            table:WonPrize ?w.
            ?w table:yearWon ?y.
        }
        GROUP BY ?w
        ORDER BY ?w""")

    winners = []
    for row in qres:
        if (category in ("%s %s %s" % row)) and (str(year) in ("%s %s %s" % row)):
            winners.append(("%s %s %s" % row).split("http", 1)[0])


    return jsonify(winners)

#/getDetails/<name>
#GET: Return details of the given nobel winner
@app.route("/getDetails/<string:name>")
def getDetails(name):
    name = name.replace("-", " ")
    qres = g.query(
    """
    PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT ?n ?nt ?b ?p ?w ?y
    {
        ?g rdf:type table:PersonWinner;
        table:name ?n;
        table:nationality ?nt;
        table:birthYear ?b;
        table:photo ?p;
        table:WonPrize ?w.
        ?w table:yearWon ?y;
        
    }
    """)
    result = {
        "name": name,
        "nationality": 'not found',
        "category": 'not found',
        "year": 0000,
        "association": 'not found',
        "born": 0000,
        "died": 0000,
        "motivation": 'not found',
        "photo": 'not found'
    }
    for row in qres:
        if name in str(row.asdict()['n'].toPython()):
            result["nationality"] = str(row.asdict()['nt'].toPython()).split('/')[-1]
            result["born"] = str(row.asdict()['b'].toPython())
            result["photo"] = str(row.asdict()['p'].toPython())
            result["category"] = str(row.asdict()['w'].toPython()).split('/')[-4]
            result["year"] = str(row.asdict()['y'].toPython())


    qres2 = g.query(
        """
        PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT ?n ?a
            {
                ?g rdf:type table:PersonWinner;
                table:name ?n;
                table:Association ?a.
            }
        """)

    for row in qres2:
        if name in str(row.asdict()['n'].toPython()):
            result["association"] = str(row.asdict()['a'].toPython()).split('#',1)[-1]


    qres3 = g.query(
    """
    PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT ?n ?d
        {
            ?g rdf:type table:PersonWinner;
            table:name ?n;
            table:deathYear ?d.
        }
    """)


    for row in qres3:
        if name in str(row.asdict()['n'].toPython()):
            result["died"] = str(row.asdict()['d'].toPython())


    qres4 = g.query(
        """
        PREFIX table:<http://swat.cse.lehigh.edu/resources/onto/nobel.owl#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT ?n ?m
        {
            ?g rdf:type table:PersonWinner;
            table:name ?n;
            table:WonPrize ?w.
        ?w table:motivation ?m;
        }
        """)

    for row in qres4:
        if name in str(row.asdict()['n'].toPython()):
            result["motivation"] = str(row.asdict()['m'].toPython())

    return jsonify(result)



#Port Number = 8000
if __name__ == "__main__":
    app.run(debug=True,port=8000)