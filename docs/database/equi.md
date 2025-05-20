# SQL

## JOIN

### EQUI JOIN -> 4th video

 ---------------

 ```sql
 SELECT e.name, e.sal, e.job, d.name, d.loc, i.*
        FROM emp e, dept d, incr i
        WHERE e.job = 'MANAGER' AND I.INGD = 'i3'
        AND e.dptno = d.depno
 ```

- INCR table not related to othere table that why we cannot apply INNER JOIN, So we are using EQUI JOIN

### INNER JOIN

```sql
 SELECT e.name, e.sal, e.job, d.*
 FROM emp e INNER JOIN dept d
 WHERE e.job = 'CLERK'`
```

- `WHERE` clase is used to write filter condion and `ON` close is used to write join condtion.
- we are use JOIN & WHERE both in INNER JOIN

### SELF JOIN

Q. Who is working like martin

```sql
SELECT e2.ename, e2.sal, e2.job, e.deptno
FROM emp e1, emp e2
AND
e1.job == e2.job
```

#### Q Display emp data Who is working in department whew sumit is working?

```sql
SELECT b.* FROM emp a, emp b
WHERE a.ename = 'SMITH'
AND
a.deptno = b.dept.no
```

> - if we select `a.*` (first table) it display duplicate data

### Inner join vs equi

- INNER JOIN is similar to EQUI JOIN
- In case of INNER JOIN query in between two tables we should specify INNER JOIN keyword
- the `JOIN` condtion you should specify by using `ON` Clause
- If you want to specify filter conditions we should specify under `WHERE` Close at the end of query

### Q. Which case we should use INNER JOIN

IF you want to use EQUI-JOIN output in Outer JOIN query we need EQUI JOIN OUTPUT
in OUTTER JOIN query in such case Dont not use EQUI JOIN query becaouse EQUI JOIN support

- WHERE CLAUSE and OUTTER JOIN SUPPORT ON CLAUSE so both aare incompatible
- If you need INNER JOIN along with OUTTER JOIN or EQUI JOIN output along with OUTTER JOIN
- We should use INNER JOIN only becaouse INNER JOIN Support `ON` CLAUSE and OUTTER JOIN alse support `ON` CLAUSE

### OUTTER JOIN

- Display all data from one table and only matched data from other table

### Three types of OUTTER JOIN

1. LEFT OUTTER JOIN OR LEF JOIN
    - All data from left table + only matched data from right table.
2. RIGHT OUTTER JOIN OR RIGHT JOIN
    - All data from Right table + only matched data from left table
3. FULL OUTER JOIN (OR) FULL JOIN

    - Matched data from both tables + unmatched data from left table, unmatched data from Right table

- Join condition should be specified byusing `ON` Clouse
- getting all the data from both table

Syntax
----------;

```sql
SELECT Col .......
FROM table1
ON <JOIN Cond>
WHERE <FILTER COND>
ORDER BY ......
```

- company_table -> compid, compname
- prod -> pid,pname,cost,msg,disk,compid

### JOIN queries

```sql
SELECT p.pid, p.name, c.pid,c.compname
FROM prod p INNER JOIN
comp c
ON p.compid = c.compid
ADD output image here

--  LEFT JOIN
SELECT p.pid, p.name, c.*
FROM prod p LEFT JOIN comp c
ON p.compid = c.compid
add output here

-- RIGHT JOIN
SELECT p.pid, p.name, c.compid 
FROM prod p RIGHT JOIN
com c
ON p.compid = c.compid

-- FULL JOIN 
SELECT p.pid, p.name, c.*
FROM prod p FULL JOIN comp c
ON p.comid = c.comid

--
CREATE table deptcp
AS
SELECT * FROM dept;

-- 
UPDATE empcp SET depno = null
WHERE depno = 30;
commit
```

##  lter table empcp drop column colmuns

```sql
SELECT e.ename, e.sal, e.deptno, d.deptno, d.name
FROM empcp e INNER JOIN deptcp d
ON e.deptno = d.deptno;

----------------------------------------

SELECT e.ename, e.sal, e.deptno, d.deptno, d.dname
FROM empcp e LEFT JOIN deptcp d
ON e.deptnp= d.deptno;
```
