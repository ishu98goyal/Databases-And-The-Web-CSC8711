distinct-values(for $d in db:open("drinks")/pubsData/drinkers/dname,
     $b in db:open("drinks")/pubsData/frequents/freq[@dname=$d]/bname,
     $r in db:open("drinks")/pubsData/serves/serve[@bname = $b]/rname
where $r = db:open("drinks")/pubsData/likes/like[@dname = $d]/rname
return $d)