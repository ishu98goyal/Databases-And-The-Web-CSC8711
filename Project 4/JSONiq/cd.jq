(: List the names of all employees who have a dependent with the same first name as themselves. :)
[
let $data := json-doc("company.json")
for $employee in $data.employees[]
for $dependent in $employee.dependents[]
where $dependent.dependentName eq $employee.fname
return $employee.fname
]