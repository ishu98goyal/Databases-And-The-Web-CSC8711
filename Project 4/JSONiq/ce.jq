(: Find the names of employees who are directly supervised by ‘Franklin Wong’. :)

[
  let $franklinssn := 
  for $emp in json-doc("company.json").employees[]
  where $emp.fname eq "Franklin"
  return $emp.ssn
for $employee in json-doc("company.json").employees[]
where $employee.supervisor eq $franklinssn
return $employee.fname || " " || $employee.lname
]