%%sqlite

USE employees;

SELECT * FROM EMPLOYEES
LIMIT 20;


-- 1 How many emp with each title where born after 1965-01-01. HEATH YOU NEED TO FINISH THIS QUESTION
SELECT count( * ) AS number_of_Emp, t.title
from employees e
INNER JOIN titles t on t.emp_no = e.emp_no
where e.birth_date > '1965-01-01'
group by t.title;

-- 2 AVerage salary per title 
SELECT ROUND( AVG ( s.salary ), 2 ) AS 'Average_Salary', t.title AS 'Title'
FROM salaries s 
INNER JOIN titles t ON s.emp_no = t.emp_no
GROUP BY t.title;

-- 3 How much money was spent on the marketing department between the years 1990 and 1992

SELECT sum( s.salary ), d.dept_name
FROM salaries s
INNER JOIN dept_emp de on s.emp_no = de.emp_no
inner join departments d on d.dept_no = de.dept_no
where d.dept_name = 'Marketing'
and year( s.from_date ) <= 1992 and year( s.to_date ) >- 1988;