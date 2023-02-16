let $movies := db:open("mdb")/mdb/movies/movie
for $movie in $movies
where $movie/cast/performer/actor[@idref = "jamescaan"]
return
  <result>
    {$movie/title}
    {$movie/year}
  </result>