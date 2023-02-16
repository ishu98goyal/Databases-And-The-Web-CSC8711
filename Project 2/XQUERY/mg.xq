for $performer in db:open("mdb")//performer
where 
  some $actor in db:open("mdb")//performer[dob < $performer/dob] 
  satisfies $actor/actedin/movie[@idref = $performer/directed/movie/@idref]
return distinct-values($performer/name)