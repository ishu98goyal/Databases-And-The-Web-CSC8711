for $performer in  db:open("mdb")//performer
let $dob := xs:date($performer/dob)
where $dob = max(db:open("mdb")//performer/xs:date(dob))
return $performer/name/text()