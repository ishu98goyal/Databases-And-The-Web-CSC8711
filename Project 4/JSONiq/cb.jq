(: Find the names of employees who work on all the projects controlled by department number 5. :)

[
  let $pro5 := 
  (for $proj in json-doc("company.json").projects[]
  where $proj.controllingDepartment eq 5
  return $proj.workers[].essn)
for $emp in json-doc("company.json").employees[]
where some $p in $pro5 satisfies $emp.ssn eq $p
return $emp.fname || " " || $emp.lname
]