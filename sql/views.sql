.mode column
.headers on

.print -----------------------------------------------------
.print -- Employees with salary greather than their chiefs
.print -----------------------------------------------------
DROP VIEW IF EXISTS expensive_employee;
CREATE VIEW expensive_employee
AS
    SELECT
        emp.name     AS emp
      , emp.salary   AS emp_salary
      , chief.name   AS chief
      , chief.salary AS chief_salary
    FROM employee AS emp
    JOIN employee AS chief
        ON  chief.id = emp.chief_id
    WHERE
        emp.salary > chief.salary
;
    
SELECT *
FROM expensive_employee;


.print -----------------------------------------------------
.print -- Employees with max salary by department
.print -----------------------------------------------------
DROP VIEW IF EXISTS department_leaders;
CREATE VIEW department_leaders
AS
    SELECT
        emp.name    AS name
      , dep.name    AS department
      , emp.salary  AS salary      
    FROM employee AS emp
    JOIN (
        -- Max salary by department
        SELECT
            emp.department_id AS department_id
          , MAX(emp.salary)   AS max_salary
        FROM employee AS emp
        GROUP BY
            emp.department_id
    ) AS dep_max
        ON  dep_max.department_id = emp.department_id
    JOIN department AS dep
        ON  dep.id = emp.department_id
    WHERE
        dep_max.max_salary = emp.salary
;

SELECT *
FROM department_leaders;


.print -----------------------------------------------------
.print -- Smallest departments
.print -----------------------------------------------------
DROP VIEW IF EXISTS smallest_departments;
CREATE VIEW smallest_departments
AS
    SELECT
        emp.department_id
    FROM employee AS emp
    GROUP BY
        emp.department_id
    HAVING
        COUNT(1) <= 3
;

SELECT *
FROM smallest_departments;


.print -----------------------------------------------------
.print -- Employees without a chief in the same department
.print -----------------------------------------------------
DROP VIEW IF EXISTS loafers;
CREATE VIEW loafers
AS
    SELECT
        emp.id
    FROM employee AS emp
    JOIN employee AS chief
        ON  chief.id = emp.chief_id
    WHERE
        chief.department_id <> emp.department_id
;

SELECT *
FROM loafers;


.print -----------------------------------------------------
.print -- Departments with a max summary salary
.print -----------------------------------------------------
DROP VIEW IF EXISTS max_departments;
CREATE VIEW max_departments
AS
    SELECT
        emp.department_id AS department_id
      , SUM(emp.salary)   AS sum_salary
    FROM employee AS emp
    GROUP BY
        emp.department_id
    ORDER BY
        sum_salary DESC
    LIMIT 1
;

SELECT *
FROM max_departments    
