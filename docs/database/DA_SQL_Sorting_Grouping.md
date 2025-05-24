# Grouping (Filtring)

## Objectives

After completing this lab, you will be able to:

1. Filter the output of a SELECT query by using string patterns, ranges, or sets of values.
2. Sort the result set in either ascending or descending order in accordance with a pre-determined column.
3. Group the outcomes of a query based on a selected parameter to further refine the response.

%load_ext sql
%sql sqlite:///HR.db

```sql
%%sql

CREATE TABLE EMPLOYEES (
                            EMP_ID CHAR(9) NOT NULL, 
                            F_NAME VARCHAR(15) NOT NULL,
                            L_NAME VARCHAR(15) NOT NULL,
                            SSN CHAR(9),
                            B_DATE DATE,
                            SEX CHAR,
                            ADDRESS VARCHAR(30),
                            JOB_ID CHAR(9),
                            SALARY DECIMAL(10,2),
                            MANAGER_ID CHAR(9),
                            DEP_ID CHAR(9) NOT NULL,
                            PRIMARY KEY (EMP_ID));
                            
  CREATE TABLE JOB_HISTORY (
                            EMPL_ID CHAR(9) NOT NULL, 
                            START_DATE DATE,
                            JOBS_ID CHAR(9) NOT NULL,
                            DEPT_ID CHAR(9),
                            PRIMARY KEY (EMPL_ID,JOBS_ID));
 
 CREATE TABLE JOBS (
                            JOB_IDENT CHAR(9) NOT NULL, 
                            JOB_TITLE VARCHAR(30),
                            MIN_SALARY DECIMAL(10,2),
                            MAX_SALARY DECIMAL(10,2),
                            PRIMARY KEY (JOB_IDENT));

CREATE TABLE DEPARTMENTS (
                            DEPT_ID_DEP CHAR(9) NOT NULL, 
                            DEP_NAME VARCHAR(15) ,
                            MANAGER_ID CHAR(9),
                            LOC_ID CHAR(9),
                            PRIMARY KEY (DEPT_ID_DEP));

CREATE TABLE LOCATIONS (
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));
```

```sql
%%sql

Insert into JOB_HISTORY (EMPL_ID, START_DATE, JOBS_ID, DEPT_ID)
VALUES 
("E1001",2000-08-01,100,2),
("E1002",2001-08-01,200,5),
("E1003",2001-08-16,300,5),
("E1004",2000-08-16,400,5),
("E1005",2000-05-30,500,2),
("E1006",2001-08-16,600,2),
("E1007",2002-05-30,650,7),
("E1008",2010-05-06,660,7),
("E1009",2016-08-16,234,7),
("E1010",2016-08-16,220,5);

%%sql

Insert into LOCATIONS (LOCT_ID, DEP_ID_LOC)
VALUES
('L0001',2),
('L0002',5),
('L0003',7)

%%sql

Insert into EMPLOYEES (EMP_ID, F_NAME, L_NAME, SSN, B_DATE, SEX, ADDRESS, JOB_ID, SALARY,MANAGER_ID,DEP_ID)
VALUES
("E1001","John","Thomas",123456,1976-09-01,"M","5631 Rice, OakPark,IL",100,100000,30001,2),
("E1002","Alice","James",123457,1972-07-31,"F","980 Berry ln, Elgin,IL",200,80000,30002,5),
("E1003","Steve","Wells",123458,1980-10-08,"M","291 Springs, Gary,IL",300,50000,30002,5),
("E1004","Santosh","Kumar",123459,1985-07-20,"M","511 Aurora Av, Aurora,IL",400,60000,30002,5),
("E1005","Ahmed","Hussain",123410,1981-04-01,"M","216 Oak Tree, Geneva,IL",500,70000,30001,2),
("E1006","Nancy","Allen",123411,1978-06-02,"F","111 Green Pl, Elgin,IL",600,90000,30001,2),
("E1007","Mary","Thomas",123412,1975-05-05,"F","100 Rose Pl, Gary,IL",650,65000,30003,7),
("E1008","Bharath","Gupta",123413,1985-06-05,"M","145 Berry Ln, Naperville,IL",660,65000,30003,7),
("E1009","Andrea","Jones",123414,1990-09-07,"F","120 Fall Creek, Gary,IL",234,70000,30003,7),
("E1010","Ann","Jacob",123415,1982-03-30,"F","111 Britany Springs,Elgin,IL",220,70000,30002,5)

%%sql

Insert into DEPARTMENTS (DEPT_ID_DEP, DEP_NAME, MANAGER_ID, LOC_ID)
VALUES
(2,"Architect Group",30001,"L0001"),
(5,"Software Group",30002,"L0002"),
(7,"Design Team",30003,"L0003")

%%sql

Insert into JOBS (JOB_IDENT, JOB_TITLE, MIN_SALARY, MAX_SALARY)
VALUES
(100,"Sr. Architect",60000,100000),
(200,"Sr. Software Developer",60000,80000),
(300,"Jr.Software Developer",40000,60000),
(400,"Jr.Software Developer",40000,60000),
(500,"Jr. Architect",50000,70000),
(600,"Lead Architect",70000,100000),
(650,"Jr. Designer",60000,70000),
(660,"Jr. Designer",60000,70000),
(234,"Sr. Designer",70000,90000),
(220,"Sr. Designer",70000,90000)

```

```sql
%%sql

SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE ADDRESS LIKE '%Elgin,IL%';
```

<table>
    <thead>
        <tr>
            <th>F_NAME</th>
            <th>L_NAME</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>James</td>
        </tr>
        <tr>
            <td>Nancy</td>
            <td>Allen</td>
        </tr>
        <tr>
            <td>Ann</td>
            <td>Jacob</td>
        </tr>
    </tbody>
</table>

## Now assume that you want to identify the employees who were born during the 70s. The query above can be modified to

```sql
%%sql

SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE B_DATE LIKE '197%';
```

<table>
    <thead>
        <tr>
            <th>F_NAME</th>
            <th>L_NAME</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ahmed</td>
            <td>Hussain</td>
        </tr>
        <tr>
            <td>Nancy</td>
            <td>Allen</td>
        </tr>
        <tr>
            <td>Bharath</td>
            <td>Gupta</td>
        </tr>
        <tr>
            <td>Andrea</td>
            <td>Jones</td>
        </tr>
    </tbody>
</table>

## Let us retrieve all employee records in department 5 where salary is between 60000 and 70000. The query that will be used is

```sql
%%sql

SELECT *
FROM EMPLOYEES
WHERE (SALARY BETWEEN 60000 AND 70000) AND DEP_ID = 5;
```

<table>
    <thead>
        <tr>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E1004</td>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>123459</td>
            <td>1958</td>
            <td>M</td>
            <td>511 Aurora Av, Aurora,IL</td>
            <td>400</td>
            <td>60000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1010</td>
            <td>Ann</td>
            <td>Jacob</td>
            <td>123415</td>
            <td>1949</td>
            <td>F</td>
            <td>111 Britany Springs,Elgin,IL</td>
            <td>220</td>
            <td>70000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
    </tbody>
</table>

## Sorting

retrieve a list of employees ordered by department ID.

```sql
%%sql
SELECT F_NAME, L_NAME, DEP_ID 
FROM EMPLOYEES
ORDER BY DEP_ID;
```

<table>
    <thead>
        <tr>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>Thomas</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Ahmed</td>
            <td>Hussain</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Nancy</td>
            <td>Allen</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Alice</td>
            <td>James</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Steve</td>
            <td>Wells</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Ann</td>
            <td>Jacob</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Mary</td>
            <td>Thomas</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Bharath</td>
            <td>Gupta</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Andrea</td>
            <td>Jones</td>
            <td>7</td>
        </tr>
    </tbody>
</table>

## the records should be ordered in descending alphabetical order by last name. For descending order, you can make use of the DESC clause

```sql
%%sql

SELECT F_NAME, L_NAME, DEP_ID 
FROM EMPLOYEES
ORDER BY DEP_ID DESC, L_NAME DESC;
```

<table>
    <thead>
        <tr>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Mary</td>
            <td>Thomas</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Andrea</td>
            <td>Jones</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Bharath</td>
            <td>Gupta</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Steve</td>
            <td>Wells</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Alice</td>
            <td>James</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Ann</td>
            <td>Jacob</td>
            <td>5</td>
        </tr>
        <tr>
            <td>John</td>
            <td>Thomas</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Ahmed</td>
            <td>Hussain</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Nancy</td>
            <td>Allen</td>
            <td>2</td>
        </tr>
    </tbody>
</table>

## Grouping

AVG is a function that can be used to calculate the Average or Mean of all values of a specified column in the result set.

- A good example of grouping would be if For each department ID, we wish to retrieve the number of employees in the department.

```sql
%%sql

SELECT DEP_ID, COUNT(*)
FROM EMPLOYEES
GROUP BY DEP_ID;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>COUNT(*)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
        </tr>
    </tbody>
</table>

### retrieve the number of employees in the department and the average employee salary in the department

```sql
%%sql
SELECT DEP_ID, COUNT(*), AVG(SALARY)
FROM EMPLOYEES
GROUP BY DEP_ID;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>COUNT(*)</th>
            <th>AVG(SALARY)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
    </tbody>
</table>

### Label the computed columns in the result set of the last problem as NUM_EMPLOYEES and AVG_SALARY

```sql
%%sql

SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>NUM_EMPLOYEES</th>
            <th>AVG_SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
    </tbody>
</table>

### e can sort the result of the previous query by average salary

```sql
%%sql

SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
ORDER BY AVG_SALARY;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>NUM_EMPLOYEES</th>
            <th>AVG_SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5</td>
            <td>4</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
    </tbody>
</table>

### we wish to limit the result to departments with fewer than 4 employees

```sql
%%sql

SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING count(*) < 4
ORDER BY AVG_SALARY;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>NUM_EMPLOYEES</th>
            <th>AVG_SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
    </tbody>
</table>

## Practice Questions

### 1.Retrieve the list of all employees, first and last names, whose first names start with ‘S’

```sql
%%sql
SELECT F_NAME, L_NAME
FROM EMPLOYEES
where F_NAME like 'S%';
```

<table>
    <thead>
        <tr>
            <th>F_NAME</th>
            <th>L_NAME</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Steve</td>
            <td>Wells</td>
        </tr>
        <tr>
            <td>Santosh</td>
            <td>Kumar</td>
        </tr>
    </tbody>
</table>

### 2. Arrange all the records of the EMPLOYEES table in ascending order of the date of birth

```sql
%%sql

SELECT* FROM EMPLOYEES
ORDER BY B_DATE
```

<table>
    <thead>
        <tr>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E1002</td>
            <td>Alice</td>
            <td>James</td>
            <td>123457</td>
            <td>1934</td>
            <td>F</td>
            <td>980 Berry ln, Elgin,IL</td>
            <td>200</td>
            <td>80000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1010</td>
            <td>Ann</td>
            <td>Jacob</td>
            <td>123415</td>
            <td>1949</td>
            <td>F</td>
            <td>111 Britany Springs,Elgin,IL</td>
            <td>220</td>
            <td>70000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1004</td>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>123459</td>
            <td>1958</td>
            <td>M</td>
            <td>511 Aurora Av, Aurora,IL</td>
            <td>400</td>
            <td>60000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1003</td>
            <td>Steve</td>
            <td>Wells</td>
            <td>123458</td>
            <td>1962</td>
            <td>M</td>
            <td>291 Springs, Gary,IL</td>
            <td>300</td>
            <td>50000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1007</td>
            <td>Mary</td>
            <td>Thomas</td>
            <td>123412</td>
            <td>1965</td>
            <td>F</td>
            <td>100 Rose Pl, Gary,IL</td>
            <td>650</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>E1001</td>
            <td>John</td>
            <td>Thomas</td>
            <td>123456</td>
            <td>1966</td>
            <td>M</td>
            <td>5631 Rice, OakPark,IL</td>
            <td>100</td>
            <td>100000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1006</td>
            <td>Nancy</td>
            <td>Allen</td>
            <td>123411</td>
            <td>1970</td>
            <td>F</td>
            <td>111 Green Pl, Elgin,IL</td>
            <td>600</td>
            <td>90000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1008</td>
            <td>Bharath</td>
            <td>Gupta</td>
            <td>123413</td>
            <td>1974</td>
            <td>M</td>
            <td>145 Berry Ln, Naperville,IL</td>
            <td>660</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>E1009</td>
            <td>Andrea</td>
            <td>Jones</td>
            <td>123414</td>
            <td>1974</td>
            <td>F</td>
            <td>120 Fall Creek, Gary,IL</td>
            <td>234</td>
            <td>70000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>E1005</td>
            <td>Ahmed</td>
            <td>Hussain</td>
            <td>123410</td>
            <td>1976</td>
            <td>M</td>
            <td>216 Oak Tree, Geneva,IL</td>
            <td>500</td>
            <td>70000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
    </tbody>
</table>

### 3. Group the records in terms of the department IDs and filter them of ones that have average salary more than or equal to 60000. Display the department ID and the average salary

```sql
%%sql
SELECT DEP_ID,AVG(SALARY) as avg_salary from EMPLOYEES
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>avg_salary</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>86666.66666666667</td>
        </tr>
        <tr>
            <td>5</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>66666.66666666667</td>
        </tr>
    </tbody>
</table>

### For the problem above, sort the results for each group in descending order of average salary

```sql
%%sql
SELECT DEP_ID,AVG(SALARY) as avg_salary from EMPLOYEES
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000
order by AVG(SALARY) desc
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>avg_salary</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>86666.66666666667</td>
        </tr>
        <tr>
            <td>7</td>
            <td>66666.66666666667</td>
        </tr>
        <tr>
            <td>5</td>
            <td>65000.0</td>
        </tr>
    </tbody>
</table>

### Exercise 1: String Patterns

### 1. Retrieve all employees whose address is in Elgin,IL

```sql
%%sql

select * from Employees
where address like "%Elgin,IL%"
```

<table>
    <thead>
        <tr>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E1002</td>
            <td>Alice</td>
            <td>James</td>
            <td>123457</td>
            <td>1934</td>
            <td>F</td>
            <td>980 Berry ln, Elgin,IL</td>
            <td>200</td>
            <td>80000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1006</td>
            <td>Nancy</td>
            <td>Allen</td>
            <td>123411</td>
            <td>1970</td>
            <td>F</td>
            <td>111 Green Pl, Elgin,IL</td>
            <td>600</td>
            <td>90000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1010</td>
            <td>Ann</td>
            <td>Jacob</td>
            <td>123415</td>
            <td>1949</td>
            <td>F</td>
            <td>111 Britany Springs,Elgin,IL</td>
            <td>220</td>
            <td>70000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
    </tbody>
</table>

### 2. Retrieve all employees who were born during the 1970’s

```sql
%%sql

select * from Employees
where B_DATE like "197%"
```

<table>
    <thead>
        <tr>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E1005</td>
            <td>Ahmed</td>
            <td>Hussain</td>
            <td>123410</td>
            <td>1976</td>
            <td>M</td>
            <td>216 Oak Tree, Geneva,IL</td>
            <td>500</td>
            <td>70000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1006</td>
            <td>Nancy</td>
            <td>Allen</td>
            <td>123411</td>
            <td>1970</td>
            <td>F</td>
            <td>111 Green Pl, Elgin,IL</td>
            <td>600</td>
            <td>90000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1008</td>
            <td>Bharath</td>
            <td>Gupta</td>
            <td>123413</td>
            <td>1974</td>
            <td>M</td>
            <td>145 Berry Ln, Naperville,IL</td>
            <td>660</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>E1009</td>
            <td>Andrea</td>
            <td>Jones</td>
            <td>123414</td>
            <td>1974</td>
            <td>F</td>
            <td>120 Fall Creek, Gary,IL</td>
            <td>234</td>
            <td>70000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
    </tbody>
</table>

### 3. Retrieve all employees in department 5 whose salary is between 60000 and 70000

```sql
%%sql

select * from Employees
where DEP_ID =5 and salary between 60000 and 70000
```

<table>
    <thead>
        <tr>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E1004</td>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>123459</td>
            <td>1958</td>
            <td>M</td>
            <td>511 Aurora Av, Aurora,IL</td>
            <td>400</td>
            <td>60000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1010</td>
            <td>Ann</td>
            <td>Jacob</td>
            <td>123415</td>
            <td>1949</td>
            <td>F</td>
            <td>111 Britany Springs,Elgin,IL</td>
            <td>220</td>
            <td>70000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
    </tbody>
</table>

### Exercise 2: Sorting

### Retrieve a list of employees ordered by department ID

```sql
%%sql
select * from employees
Order by DEP_ID
```

<table>
    <thead>
        <tr>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E1001</td>
            <td>John</td>
            <td>Thomas</td>
            <td>123456</td>
            <td>1966</td>
            <td>M</td>
            <td>5631 Rice, OakPark,IL</td>
            <td>100</td>
            <td>100000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1005</td>
            <td>Ahmed</td>
            <td>Hussain</td>
            <td>123410</td>
            <td>1976</td>
            <td>M</td>
            <td>216 Oak Tree, Geneva,IL</td>
            <td>500</td>
            <td>70000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1006</td>
            <td>Nancy</td>
            <td>Allen</td>
            <td>123411</td>
            <td>1970</td>
            <td>F</td>
            <td>111 Green Pl, Elgin,IL</td>
            <td>600</td>
            <td>90000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>E1002</td>
            <td>Alice</td>
            <td>James</td>
            <td>123457</td>
            <td>1934</td>
            <td>F</td>
            <td>980 Berry ln, Elgin,IL</td>
            <td>200</td>
            <td>80000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1003</td>
            <td>Steve</td>
            <td>Wells</td>
            <td>123458</td>
            <td>1962</td>
            <td>M</td>
            <td>291 Springs, Gary,IL</td>
            <td>300</td>
            <td>50000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1004</td>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>123459</td>
            <td>1958</td>
            <td>M</td>
            <td>511 Aurora Av, Aurora,IL</td>
            <td>400</td>
            <td>60000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1010</td>
            <td>Ann</td>
            <td>Jacob</td>
            <td>123415</td>
            <td>1949</td>
            <td>F</td>
            <td>111 Britany Springs,Elgin,IL</td>
            <td>220</td>
            <td>70000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>E1007</td>
            <td>Mary</td>
            <td>Thomas</td>
            <td>123412</td>
            <td>1965</td>
            <td>F</td>
            <td>100 Rose Pl, Gary,IL</td>
            <td>650</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>E1008</td>
            <td>Bharath</td>
            <td>Gupta</td>
            <td>123413</td>
            <td>1974</td>
            <td>M</td>
            <td>145 Berry Ln, Naperville,IL</td>
            <td>660</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>E1009</td>
            <td>Andrea</td>
            <td>Jones</td>
            <td>123414</td>
            <td>1974</td>
            <td>F</td>
            <td>120 Fall Creek, Gary,IL</td>
            <td>234</td>
            <td>70000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
    </tbody>
</table>

### 2. Retrieve a list of employees ordered by department name, and within each department ordered alphabetically in descending order by last name

```sql
%%sql

select * from departments,employees
WHERE DEP_ID = DEPT_ID_DEP

Order by DEP_NAME,L_NAME   desc
```

<table>
    <thead>
        <tr>
            <th>DEPT_ID_DEP</th>
            <th>DEP_NAME</th>
            <th>MANAGER_ID</th>
            <th>LOC_ID</th>
            <th>EMP_ID</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
            <th>SSN</th>
            <th>B_DATE</th>
            <th>SEX</th>
            <th>ADDRESS</th>
            <th>JOB_ID</th>
            <th>SALARY</th>
            <th>MANAGER_ID_1</th>
            <th>DEP_ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>Architect Group</td>
            <td>30001</td>
            <td>L0001</td>
            <td>E1001</td>
            <td>John</td>
            <td>Thomas</td>
            <td>123456</td>
            <td>1966</td>
            <td>M</td>
            <td>5631 Rice, OakPark,IL</td>
            <td>100</td>
            <td>100000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Architect Group</td>
            <td>30001</td>
            <td>L0001</td>
            <td>E1005</td>
            <td>Ahmed</td>
            <td>Hussain</td>
            <td>123410</td>
            <td>1976</td>
            <td>M</td>
            <td>216 Oak Tree, Geneva,IL</td>
            <td>500</td>
            <td>70000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Architect Group</td>
            <td>30001</td>
            <td>L0001</td>
            <td>E1006</td>
            <td>Nancy</td>
            <td>Allen</td>
            <td>123411</td>
            <td>1970</td>
            <td>F</td>
            <td>111 Green Pl, Elgin,IL</td>
            <td>600</td>
            <td>90000</td>
            <td>30001</td>
            <td>2</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Design Team</td>
            <td>30003</td>
            <td>L0003</td>
            <td>E1007</td>
            <td>Mary</td>
            <td>Thomas</td>
            <td>123412</td>
            <td>1965</td>
            <td>F</td>
            <td>100 Rose Pl, Gary,IL</td>
            <td>650</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Design Team</td>
            <td>30003</td>
            <td>L0003</td>
            <td>E1009</td>
            <td>Andrea</td>
            <td>Jones</td>
            <td>123414</td>
            <td>1974</td>
            <td>F</td>
            <td>120 Fall Creek, Gary,IL</td>
            <td>234</td>
            <td>70000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Design Team</td>
            <td>30003</td>
            <td>L0003</td>
            <td>E1008</td>
            <td>Bharath</td>
            <td>Gupta</td>
            <td>123413</td>
            <td>1974</td>
            <td>M</td>
            <td>145 Berry Ln, Naperville,IL</td>
            <td>660</td>
            <td>65000</td>
            <td>30003</td>
            <td>7</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Software Group</td>
            <td>30002</td>
            <td>L0002</td>
            <td>E1003</td>
            <td>Steve</td>
            <td>Wells</td>
            <td>123458</td>
            <td>1962</td>
            <td>M</td>
            <td>291 Springs, Gary,IL</td>
            <td>300</td>
            <td>50000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Software Group</td>
            <td>30002</td>
            <td>L0002</td>
            <td>E1004</td>
            <td>Santosh</td>
            <td>Kumar</td>
            <td>123459</td>
            <td>1958</td>
            <td>M</td>
            <td>511 Aurora Av, Aurora,IL</td>
            <td>400</td>
            <td>60000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Software Group</td>
            <td>30002</td>
            <td>L0002</td>
            <td>E1002</td>
            <td>Alice</td>
            <td>James</td>
            <td>123457</td>
            <td>1934</td>
            <td>F</td>
            <td>980 Berry ln, Elgin,IL</td>
            <td>200</td>
            <td>80000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Software Group</td>
            <td>30002</td>
            <td>L0002</td>
            <td>E1010</td>
            <td>Ann</td>
            <td>Jacob</td>
            <td>123415</td>
            <td>1949</td>
            <td>F</td>
            <td>111 Britany Springs,Elgin,IL</td>
            <td>220</td>
            <td>70000</td>
            <td>30002</td>
            <td>5</td>
        </tr>
    </tbody>
</table>

```sql
%%sql
SELECT D.DEP_NAME , E.F_NAME, E.L_NAME
FROM EMPLOYEES as E, DEPARTMENTS as D
WHERE E.DEP_ID = D.DEPT_ID_DEP
ORDER BY D.DEP_NAME, E.L_NAME DESC;
```

<table>
    <thead>
        <tr>
            <th>DEP_NAME</th>
            <th>F_NAME</th>
            <th>L_NAME</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Architect Group</td>
            <td>John</td>
            <td>Thomas</td>
        </tr>
        <tr>
            <td>Architect Group</td>
            <td>Ahmed</td>
            <td>Hussain</td>
        </tr>
        <tr>
            <td>Architect Group</td>
            <td>Nancy</td>
            <td>Allen</td>
        </tr>
        <tr>
            <td>Design Team</td>
            <td>Mary</td>
            <td>Thomas</td>
        </tr>
        <tr>
            <td>Design Team</td>
            <td>Andrea</td>
            <td>Jones</td>
        </tr>
        <tr>
            <td>Design Team</td>
            <td>Bharath</td>
            <td>Gupta</td>
        </tr>
        <tr>
            <td>Software Group</td>
            <td>Steve</td>
            <td>Wells</td>
        </tr>
        <tr>
            <td>Software Group</td>
            <td>Santosh</td>
            <td>Kumar</td>
        </tr>
        <tr>
            <td>Software Group</td>
            <td>Alice</td>
            <td>James</td>
        </tr>
        <tr>
            <td>Software Group</td>
            <td>Ann</td>
            <td>Jacob</td>
        </tr>
    </tbody>
</table>

## Exercise 3: Grouping

### 1. For each department ID retrieve the number of employees in the department

```sql
%%sql

select DEP_ID, count(*) as num_of_emp from employees
Group By DEP_ID
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>num_of_emp</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
        </tr>
    </tbody>
</table>

### For each department retrieve the number of employees in the department, and the average employee salary in the department

```sql
%%sql
select DEP_ID,count(*) as num_of_emp,AVG(SALARY) from employees
Group By DEP_ID;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>num_of_emp</th>
            <th>AVG(SALARY)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
    </tbody>
</table>

### 3. Label the computed columns in the result set of SQL problem 2 (Exercise 3 Problem 2) as NUM_EMPLOYEES and AVG_SALARY

```sql
%%sql
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>NUM_EMPLOYEES</th>
            <th>AVG_SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
    </tbody>
</table>

### In SQL problem 3 (Exercise 3 Problem 3), order the result set by Average Salary

```sql
%%sql
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
ORDER BY AVG_SALARY;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>NUM_EMPLOYEES</th>
            <th>AVG_SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5</td>
            <td>4</td>
            <td>65000.0</td>
        </tr>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
    </tbody>
</table>

### In SQL problem 4 (Exercise 3 Problem 4), limit the result to departments with fewer than 4 employees

```sql
%%sql
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING count(*) < 4
ORDER BY AVG_SALARY;
```

<table>
    <thead>
        <tr>
            <th>DEP_ID</th>
            <th>NUM_EMPLOYEES</th>
            <th>AVG_SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>7</td>
            <td>3</td>
            <td>66666.66666666667</td>
        </tr>
        <tr>
            <td>2</td>
            <td>3</td>
            <td>86666.66666666667</td>
        </tr>
    </tbody>
</table>

### You want to select the author's lastname from a table, but you only remember that it starts with the letter J. Which of the following queries uses the correct string pattern?

```sql
SELECT lastname from author where lastname like ‘J%’ 

SELECT lastname from author where lastname like ‘J*’ 

SELECT lastname from author where lastname like ‘J$’ 

SELECT lastname from author where lastname like ‘J#’ 
```

### Question 2 In SQL, which of the following will be the correct way to sort a result set in descending order?

```sql

SELECT ID FROM TABLE_NAME ORDER BY ID DESC 

SELECT * FROM TABLE_NAME ORDER BY ID DESC 

SELECT * FROM TABLE_NAME ORDER BY ID 

SELECT ID FROM TABLE_NAME ORDER BY ID 
```

What is the role of HAVING clause in SQL queries in MySQL?

Acts as an alternative to WHERE clause in SQL queries.
 It may not necessarily organize the result set in a specific order.
Check whether data records meet the specified condition is met or not.
Restricts the result set for a query using GROUP BY clause.

### Question 4 Which of the choices best describe the function of the following SQL query?

```sql

SELECT * FROM employees ORDER BY emp_name LIMIT 5; 
```

Retrieves all the columns of the top 5 rows of the table, sorted alphabetically based on emp_names

Retrieves all the columns of the top 5 rows of the table, sorted reverse alphabetically based on emp_names

Retrieves the entire contents of the table, sorted alphabetically based on emp_names

Retrieves the top 5 emp_names ordered alphabetically.

### Question 5 Which of the following SQL statements lists the number of customers in each country, showing only the countries with more than five customers?

```sql

SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING CustomerID > 5; 

SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) > 5; 

SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) < 5; 

SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(Customers) > 5; 
```
