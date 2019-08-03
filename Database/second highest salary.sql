---check points: subquery in where clause; use of max
select max(salary) as "SecondHighestSalary"
from employee
where salary < (select max(salary) from employee order by salary)