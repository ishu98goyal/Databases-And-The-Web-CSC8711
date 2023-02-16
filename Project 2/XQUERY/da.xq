distinct-values(for $b in db:open("drinks")//bars/bname,
    $s in db:open("drinks")//serves/serve[@bname = $b],
    $l in db:open("drinks")//likes/like[@dname = "Donald"]/rname
where $s/rname = $l
return $b)