for $performer in db:open("mdb")/mdb/performers/performer
where $performer/directed/movie/@idref = $performer/actedin/movie/@idref
return $performer/name/text()
