for $performer in db:open("mdb")/mdb/performers/performer
let $movies := count($performer/actedin/movie)
return concat($performer/name, " has acted in ", $movies, " movies")
