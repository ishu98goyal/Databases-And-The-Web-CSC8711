for $drinker in db:open("drinks")/pubsData/drinkers/dname,
    $donald_bar in db:open("drinks")/pubsData/frequents/freq[@dname="Donald"]/bname,
    $drinker_bar in db:open("drinks")/pubsData/frequents/freq[@dname=$drinker]/bname
where $donald_bar = $drinker_bar and $drinker != "Donald"
return distinct-values($drinker)