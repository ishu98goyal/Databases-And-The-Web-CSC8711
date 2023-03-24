(: Retrieve the names and addresses of all employees who work on at least one project located in Houston but whose department has no location in Houston. :)

[
let $data := json-doc("company.json")
let $houstonPro := (
    for $project in $data.projects[] 
            where $project.plocation eq "Houston" 
    return $project.pnumber
)
let $depNoHouston := (
    for $department in $data.departments[] 
        where every $location in $department.locations[] 
        satisfies $location ne "Houston" 
    return $department.dno
)
let $depNoHoustonEmp := (
    for $employee in $data.employees[],
        $dept in $depNoHouston
            where $employee.worksFor eq $dept
    return $employee
)
let $finalEmps := (
    for $emp in $depNoHoustonEmp
    where some $prj in $houstonPro, $empPrj in $emp.projects[]
        satisfies $prj eq number($empPrj.pno)
    return $emp.fname || " " || $emp.lname || ": " || $emp.address
)
return $finalEmps
]