for $d in db:open("drinks")/pubsData/drinkers/dname,
    $f in db:open("drinks")/pubsData/frequents/freq[@dname = $d],
    $l in db:open("drinks")/pubsData/likes/like[@dname = $d]
where every $b in $f/bname 
      satisfies some $r in db:open("drinks")/pubsData/serves/serve[@bname = $b]/rname 
      satisfies $r = $l/rname
return distinct-values($d)