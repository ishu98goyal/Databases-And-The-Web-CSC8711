distinct-values(for $d in db:open("drinks")/pubsData/drinkers/dname,
$f in db:open("drinks")/pubsData/frequents/freq[@dname = $d]/bname,
$b in db:open("drinks")/pubsData/serves/serve[@bname = $f]/rname
let $l := db:open("drinks")/pubsData/likes/like[@dname = $d]/rname
where not(some $r in $l satisfies $r = $b)
return $d)