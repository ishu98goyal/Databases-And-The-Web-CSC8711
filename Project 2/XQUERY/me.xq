for $p in distinct-values(db:open("mdb")/mdb/performers/performer/[@id])
let $performer := db:open("mdb")/mdb/performers/performer
let $moviesActedIn := count(db:open("mdb")/mdb/movies/movie/cast/performer/actor[@idref = $p])
let $moviesDirected := count(db:open("mdb")/mdb/performers/performer[@id=$p]/directed/movie)
where $moviesActedIn >= 10 and $moviesDirected >= 2
return concat($performer[@id=$p]/name, " has acted in ", $moviesActedIn, " movies and directed ", $moviesDirected, " movies.")
