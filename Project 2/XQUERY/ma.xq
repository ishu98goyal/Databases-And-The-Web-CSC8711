let $movies := db:open("mdb")/mdb/movies/movie
for $movie in $movies
where $movie/genres/genre = "Crime"
return
  <movie>
    <title>{$movie/title/text()}</title>
    <year>{$movie/year/text()}</year>
  </movie>