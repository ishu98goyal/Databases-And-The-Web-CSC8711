(: List the names of all employees with two or more dependents. :)

[for $emp in json-doc("company.json").employees[]
where count($emp.dependents[]) gt 1
return $emp.fname  || " " || $emp.lname
]