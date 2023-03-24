(: Retrieve the name and address of employees who work for the "Research" department. :)

[
        for $emp in json-doc("company.json").employees[], 
        $dept in json-doc("company.json").departments[]
        where $emp.worksFor eq $dept.dno and $dept.dname eq "Research"
        return {
                        "Name": $emp.fname || " " || $emp.minit || ". " || $emp.lname, 
                        "Address": $emp.address
                }
]