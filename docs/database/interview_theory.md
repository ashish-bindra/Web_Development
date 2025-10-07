# Interview prepration theory part

## What is DBMS

DBMS stand for DataBase Managment System and is used to store, reterive and update data in  computer system

There are 2 types of DBMS

1. RDBMS: Relational DBMS eg. MYSQLmMSQL, PostgreSQL
2. NOSQL: Non Relational DBMS eg MongoDB, Cassandra

## SQl Statement to create a table

```sql
CREATE TABLE persion(
personID int NOTNULL,
personName varchar(50) NOT NULL,
age int,
PRIMARY KEY(persopnID)
);
```

## What is foreign Key

- A foreign kwy is a key used to link two table togather
- It is a field(or collection of fields) in one table that refer to the PRIMARY KEY in another table

```sql
CREATE TABLE order(
    orderID int not null,
    prderNumber int not null,
    customerID int,
    PRIMARY KEY(orderID),
    FOREIGN KEY(customerID) REFERENCE persson(persionID)
)
```

## Primary key vs unique key

|sno|primary key|unique key|
|---|-----------|----------|
|1|Only one primary key in a row|Multiple unique key in a row|
|2|Cannot accept null values|Can accept one null value|
|3|Create clustered index|create non-clustered index|

```sql
CREATE TABLE persion(
personID int NOTNULL,
personName varchar(50) NOT NULL,
personLastName varchar(50) NOT NULL,
age int,
PRIMARY KEY(persopnID),
UNIQUE(customerID)
```

### Supper key

Super key is an attribute (or set of attributes) that is used to uniqely identifies all attributes in a relation

### Candidate key

Candidate key is set of attribute which unique identify

## DELETE vs DROP vs Truncate

- DELETE

    It is used to delete one or more rows of a table based on a condition

    ```sql

    DELETE FROM customer WHERE customerName='XYZ';
    ```

- DROP (drop table/ drop database)

    It is used to delete the complete table or database schema is also remove

    ```SQL
    DROP TABLE logs;
    DROP DATABASE logsDB;
    ```

- Truncate

    It is used to clear the data inside the table.The table schema intract

    ```sql
    TRUNCATE TABLE logs;
    ```

## UNION vs UNIOUN ALL

- UNION

The sql SUNION clause/operator is used to combine the result of two or more select statement without any dublicate rows

A,B UNION A,C = A,B,C

- UNIOUN ALL

The unioun all operater is used to combinethe result of twol SELECT statements including dublicate rows

eg A,B unioun all A,C = A,A,B,C

## ACID Property

- A: Atomicity
- C: Consistency
- I: Isolation
- D: Durabilty

1. Atomicity
   Entire transaction take place at once or do not happen at all.

   eg

   ```yaml
    a = 15000
    b = 5000
    a = a - 5000 => 10000
    b = b + 5000 => 10000
   ```

2. Consistency
 The database must be consistent before and after the transaltion

3. Isolation
 Multiple transation happen independently without interfering with onr another. The intermediate state of a transation is invisble to other transation

4. Durability
   Once a transation has happended, the change stay there if a system failure occurance after words.

---

## Repositery

A central place in which an aggrate of is kept and maintained in an organization way usially in compute stage

## Aggreate

In db managment aggrate function is function when the value of multiple rows are grouped togather as input on certain creria to form a single value of more significant mening. like sum(), count(), avg(), min(), max()

eg

```sql
Select age, COUNT(Roll_No) as no_of_std from student GROUP BY agr HAVING COUNT(Roll_No)>1
```

### GROUP BY

is used to group row that have the same value

### Statement

Use this general pupose access to your database. Useful when you are using staic SQL staement at runtime

## Primary  vs Forgin key

|       |       primary key             | forgin key |
| ----- | ----------------------------- |------------|
|  Basic| it used to identify each records into db table unqely | It is used to link two table togather. It means forgin key in one table refer to the primary key of another |
| Null| The primary key column value can never be null| The korgin column can accept a null value|
|Dublicate| The primary key is unique attribute there cannot store dubblicate value in column| Wecan store dublicate value in the column|
|Relationship| It cannot create parent-child relationsip in a table|It can make a parent child relationship|
Deletion| Parimary key cannot be removeded from table if you want to delete it thrn make the refering frogin key doe not create its value| The forgin value removied from the table bothering thatit refer to primary key value of |

## Where class vs  Having close

| sno|Where clause| Having claouse|
|----|------------|---------------|
|1|Where clause is used to filter the records from the table based on the specificed condition|Having clause is used to filter records from the groups based on condition|
|2|Where clause can be used without GROUP BY clause|Having clause cannot be used withoud GROUP BY clause|
|3|Where clasuse implements in row operations|Having Clause implements in column operation|
|4| Where clause cannot contain aggreate function|Having clause can only control aggratr dunction|
|5|Where clause can be used with SELECT, UPDATE, DELETE statent.|Having clause can only be used with SELECT statent|
|6|WHERE clause is used before GROUP BY clause| Having clause is used after GROUP BY clause|
|7|Where clause is used with single row function like UPPER, LOWER etc|Having clause is used with multiple row function like SUN,Count|

## JOINs

- INNER JOIN

  Return records that have matching values in both tables

- LEFT

  Return all records from the left table and the match recordes from right table

- RIGHT JOIN

  Return all records from right table and matched records from left table

- FULL JOIN

  Return all records when there is not a mater in left or right tabl. THis is a UNION of LEFT and RIGHT JOIN.

## Normalization

Dublicay == Redundancy

- Normalization is the process of organizating the data in the database

- The normal form is used to reduce redundancy/ mutliple copies from the database, table or relation

- To remove insertion, updation and deletion Anomales
- It divides the larger table into the smaller table and link them using relationship

### Functional Dependency

- The attributes of table is said to be dependent on each other when an atteibute of a table unqiely identifies another attribute of same table.

- The function depency is a relationship that exists between two attributes. it typically exists between primary ley and non- key attributs with in table

eg id search name

|id:x|name:y|
|----|------|
|1|A|
|2|B|

x-> Y determent dependent

Y is functionaly depend on x beacuse we find value of y with the help of x

### 1NF

- A relation will be 1NF if it container an atomic value
- It state that an attribute of table cannot hold multiple value it must held only single value attribute
- Fist normal form dissallow the multi value attribute compossite attribute and their combination.

|id|name|mobile|
|--|----|------|
|1|A|123,123|

|id|name|mobile|
|--|----|------|
|1|A|123|
|1|A|123|

### 2NF

- Relation must be 1NF
- Relation must not contain any partail depency
- When no non-prime attribute is dependent on any proper subset of any candidate key of the table is called partailed dependcy

|id| no|fee|
|--|---|---|
|1|c1|100|
|2|c2|200|
|3|c3|100|

t1

|id| no|
|--|---|
|1|c1|
|2|c2|

|id|fee|
|--|---|
|c1| 100|
|c2|200|

### 3NF

- Relation will be in 3NF it is in 2NF
- It contain any transitive depency
- 3NF is used to achive the data integity

#### Trnsitive Depency

If a non price attribute functely dependence on on-prime attribute

### NAND as Universal gate

AND OR & NOT are sufficient to implemnt an digital system

- if we can convert NAND or NOR tothe these three we can say that any cicuit can be implemented by NAND or NOR

---

Q1. Difference between DBMS and RDBMS

RDBms

1. What is the difference between a primary key and a unique key?
Both primary and unique keys uniquely identify records in a table. However, a primary key doesn’t allow NULL values, whereas a unique key can accept NULL values.

2. What is a constraint, and why use constraints?
SQL constraints are a set of rules applied to a column or table to maintain data integrity. SQL consists of many constraints, which are as follows:

DEFAULT: It sets a default value for a column.
UNIQUE: It ensures all values are unique.
NOT NULL: It prevents NULL values.
PRIMARY KEY: It enables the unique identification of each record in a table. We can say that it combines NOT NULL and UNIQUE.
FOREIGN KEY: Links records in two tables.

## 3. What is the COALESCE function?

## 4. What are UNION, MINUS, and INTERSECT in SQL?

In SQL, UNION, MINUS, and INTERSECT are set operators used to combine or compare results from multiple SELECT queries:

UNION:
Combines the results of two SELECT statements and removes duplicate rows.
Use when you want to merge datasets without duplicates.
MINUS:
Returns rows from the first SELECT that are not found in the second.
Used to identify differences between two datasets.
INTERSECT:
Returns only the rows that are common to both SELECT statements.
Use when you need data that appears in both datasets.

## 5. What is a view in SQL, and what are its types?

A view is a virtual table representing data from one or more tables without physically storing it. It can simplify complex queries.

There are four types of views in SQL:

Simple View: It is a view based on a single table and does not have a GROUP BY clause or other SQL features.
Complex View: This is a view built from several tables and includes a GROUP BY clause as well as functions.
Inline View: It is a view built on a subquery in the FROM clause, which provides a temporary table and simplifies a complicated query.
Materialised View: This is a view that saves both the definition and the details. It builds data replicas by physically preserving them.

6. What do you understand about a temporary table? Write a query to create it.
A temporary table is a table that is created to store data temporarily during a session. It exists only while the session is active or until it is dropped manually.

It’s useful for storing intermediate results when working with complex queries or large data.

Example:

-- Create a temporary table named 'TempEmployees'
CREATE TEMPORARY TABLE TempEmployees (
    ID INT,    -- Define a column 'ID' of integer type
    Name VARCHAR(50)    -- Define a column 'Name' that can store up to 50 characters
);

7. How would you optimize a slow-moving SQL query? List the SQL optimization techniques.
You can optimize a slow-moving SQL query by using specific performance tuning techniques.

There are several SQL query optimization techniques listed below:

Use indexes on frequently filtered or joined columns.
Avoid SELECT *; select only the required columns.
Filter early with proper WHERE clauses.
Analyse the query with EXPLAIN to find bottlenecks.
Replace correlated subqueries with joins or CTEs.
Limit results using LIMIT or pagination.
Ensure efficient joins and avoid unnecessary sorting.
These steps help improve performance by reducing data scanned and optimising execution.

8. What are the different types of JOINs in SQL?
There are six different types of JOINs in SQL, which are:

INNER JOIN: An INNER JOIN is used to return records of the same value in two tables.
LEFT JOIN: LEFT JOIN is used to join all the rows in the left table with matching rows in the right table.
RIGHT JOIN: RIGHT JOIN is used to join all the rows in the right table with the corresponding rows in the left table.
FULL JOIN: A FULL JOIN is used to return all records from two tables, if there are matching records in each table.
SELF JOIN: A SELF JOIN is a join used to join a table to itself. SELF JOINS treats one table as two tables.
CARTESIAN JOIN: A CARTESIAN Integral is used to multiply the number of rows in the first table by the number of rows in the second table. It is also called a CROSS JOIN.

9. Given a Supervision table with employee_id and manager_id, write a query to detect if there is a cycle in the reporting hierarchy.
-- Use a recursive CTE to traverse the supervision hierarchy
WITH RECURSIVE Hierarchy AS (
SELECT employee_id, manager_id, employee_id AS root
FROM Supervision
UNION ALL
SELECT H.employee_id, S.manager_id, H.root
FROM Hierarchy H
JOIN Supervision S ON H.manager_id = S.employee_id
-- Avoid immediate cycles in a single step
WHERE H.root <> S.manager_id
)

-- After building the hierarchy, detect cycles
SELECT root
FROM Hierarchy
GROUP BY root

-- If the number of manager_id values is different from the number of distinct ones, it means a manager was repeated in the path, which indicates a cycle
HAVING COUNT(DISTINCT manager_id) <> COUNT(manager_id);

## Queryset

## Write an UPDATE query to set the total_sales to the sum of individual sales amounts for each employee in the employee table

-- Update the total_sales column in the employee table
UPDATE Intellipaat_Emp e
SET total_sales = (

-- Subquery to calculate the sum of sales for the specific employee
SELECT SUM(sale_amount)
FROM sales s
WHERE s.employee_id = e.employee_id
)

-- Only update if the employee has sales entries
WHERE EXISTS (
SELECT 1
FROM sales s
WHERE s.employee_id = e.employee_id
);

## 11. What are ACID properties?

ACID stands for atomicity, consistency, isolation, and durability. These properties ensure the reliable processing of database transactions.

12. What is the difference between the WHERE clause and the HAVING clause?
Aspect WHERE Clause HAVING Clause
Purpose Filters rows before grouping Filters groups after grouping
Used With SELECT, UPDATE, DELETE Only with SELECT (usually with GROUP BY)
Works On Individual rows Aggregate/grouped data
Aggregate Functions Cannot be used with aggregate functions Can be used with aggregate functions
Execution Order Evaluated before GROUP BY Evaluated after GROUP BY
Example WHERE salary > 50000 HAVING COUNT(*) > 3

## When will you use the DISTINCT keyword?

DISTINCT is used to eliminate duplicate rows.
SELECT COUNT (DISTINCT Table_name). This can be used to count the unique records.
However, using it multiple times can impact the table’s performance.

## How will you prevent SQL injection?

SQL injection can be prevented very efficiently if we use parameterized queries or prepared statements instead of dynamic SQL, where we concatenate strings.

So instead of writing:

"SELECT * FROM users WHERE id = " + user_input;
You should write:

"SELECT * FROM users WHERE id = %s"
Now, user input is only data, no matter how the code is executed. This method makes sure that even if the user decides to insert some illegal SQL commands, they will not be executed. Prepared statements are available in most SQL libraries of today, and they are regarded as the most suitable method for implementing application security against SQL injection attacks.

## 16. What is the difference between the Drop vs Delete commands?

The DROP and DELETE commands in SQL are used for removing data, but they differ significantly:

DROP: The DROP command is a DDL command. It completely removes a table or database, including its structure and all data from the database.
DELETE: Delete is a DML command. It removes specific rows of data from a table based on a given condition.

## 17. What is a trigger?

The trigger is used to do an automatic process when a particular event happens in the database or table. It helps in maintaining the integrity of the table and associated tables. The trigger can be activated when SQL commands like insert, update, and delete are fired. The syntax used to generate the trigger function is as follows:

`CREATE TRIGGER trigger_name`
18. What is normalization? Explain its types.
Normalization is used to reduce data redundancy and improve data integrity. Normalization splits the big table into multiple subtables and ensures that database integrity constraints are intact in their relationship with each other. It is a process of decomposing tables to eliminate data redundancy.

Types of normalization:

1NF: Ensures that each column contains only atomic (indivisible) values.
2NF: Remove partial dependencies.
3NF: Remove transitive dependencies.
BCNF: Ensures that every determinant is a candidate key.

## 19. What is the difference between the BETWEEN and IN operators in SQL?

The BETWEEN operator is employed to identify rows that fall within a specified range of values, encompassing numerical, textual, or date values. It returns the count of values that exist between the two defined boundaries.

On the other hand, the IN operator serves as a condition operator used for searching values within a predetermined range. When multiple values are available for selection, the IN operator is utilised.

20. What are DDL, DML, DCL, TCL, and DQL in SQL?
DDL: Data Definition Language is used to create, modify, and drop the schema of database objects. CREATE, ALTER TABLE, DROP, TRUNCATE, and ADD COLUMN are DDL commands.
DML: Data Manipulation Language allows for changing or manipulating the existing data of the tables. UPDATE, DELETE, and INSERT are DML commands.
DCL: Data Control Language allows the administrator of the database to manage the rights and permissions of the users in the database. GRANT and REVOKE are DCL commands.
TCL: Transaction Control Language is used to maintain the SQL operations within the database. It also allows the changes to be saved, which are made by the DML commands. COMMIT, SET TRANSACTION, ROLLBACK, and SAVEPOINT are examples of TCL commands.
DQL: Data Query Language is used to retrieve data from databases using the SELECT statement.

21. What is AUTO_INCREMENT?
AUTO_INCREMENT is used in SQL to automatically generate a unique number whenever a new record is inserted into a table. This is mainly used in scenarios where individual columns or groups of columns cannot be used as primary keys.

For Example:

-- Create a table named 'Employee'
CREATE TABLE Employee (

-- Use AUTO_INCREMENT to automatically generate a unique ID for each new record
Employee_id INT NOT NULL AUTO_INCREMENT,
Employee_name VARCHAR(255) NOT NULL,
Employee_designation VARCHAR(255),
Age INT,

-- Set 'Employee_id' as the AUTO_INCREMENT Primary Key of the table
PRIMARY KEY (Employee_id)
);

22. How do window functions work?
Window functions perform calculations across related rows without collapsing them like GROUP BY.

Example: RANK() OVER (PARTITION BY department ORDER BY salary DESC) ranks salaries within each department. They’re powerful for running totals, rankings, and moving averages while preserving original rows.

23. What is a subquery?
A subquery is a query nested within another query, enabling more complex data retrieval.

24. Explain the difference between a correlated subquery and a nested subquery.
Correlated Subquery: References data from the outer query in its WHERE clause.
Nested Subquery: This can be placed anywhere in the outer query and does not directly reference the outer table.
Intermediate SQL Interview Questions
In this section, we have listed the intermediate-level interview questions for the candidates who are looking to master their ability to think critically, optimize queries, and handle moderate database complexities with confidence

25. What is a function in SQL, and why do we use functions?
A function is a database object that encapsulates a set of SQL statements that perform operations and return a specific result. SQL functions are used to increase the readability and reusability of code.

26. What is the difference between the UNION and UNION ALL operators?
The UNION and UNION ALL operators are both used to combine the output of two or more SELECT queries, but they differ in handling duplicate rows:

UNION: UNION operators combine the results of multiple SELECT queries and remove duplicate rows. It returns only distinct values across all queries.
UNION ALL: The UNION ALL operator combines the output of multiple SELECT queries, including duplicates.
27. What is a stored procedure?
A stored procedure is a set of SQL statements stored in the database that can be reused, promoting modular programming.

28. Explain the GROUP BY and HAVING clauses
GROUP BY: GROUP BY aggregates data into groups based on specified columns (like department or date).

HAVING: HAVING filters these groups after aggregation, similar to WHERE for individual rows.

Example: SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 80000 shows only departments with an average salary above 60k.

29. What are the different types of SQL commands?
SQL commands are broadly classified into five categories: DDL (Data Definition Language), DML (Data Manipulation Language), DCL (Data Control Language), TCL (Transaction Control Language), and DQL (Data Query Language).

DDL consists of commands such as CREATE, ALTER, and DROP.
DML consists of INSERT, UPDATE, and DELETE.
DCL consists of GRANT and REVOKE.
TCL consists of COMMIT, ROLLBACK, and SAVEPOINT.
DQL is mainly the SELECT command.
The SQL command types are various ways to handle the database structure, perform data operations, and regulate access.

30. What is the difference between SQL and NoSQL databases?
SQL databases are relational, table-based, and normally utilize the Structured Query Language for the purposes of defining and manipulating data. Usually, they allow ACID features and are quite suitable for structured data as well as for complex queries. In contrast, NoSQL databases are non-relational, which by nature allows key-value, document, columnar, or graph formats. They are typically designed for high scalability and match unstructured or semi-structured data, thus being ideal for big data and real-time web applications.

31. What are aggregate functions in SQL?
Aggregate functions in SQL carry out a computation over a collection of values and produce a single outcome. Typical instances encompass:

COUNT(): Returns the number of rows.
SUM(): Returns the total sum.
AVG(): Returns the average value.
MIN() / MAX(): Return the minimum or maximum value, respectively.
32. What are indexed views?
An indexed view is a view in SQL that has a unique clustered index created on it, thus only the data of the view result is physically stored on the disk. In comparison to traditional views, indexed views improve performance by calculating the joins and aggregations before execution. Indexed views are most beneficial in SQL Server to improve performance in OLAP scenarios.

33. What are the different isolation levels in SQL?
SQL supports five isolation levels to handle concurrency in transactions:

Read Uncommitted: Allows dirty reads.
Read Committed: Default in most databases, and it avoids dirty reads.
Repeatable Read: Prevents dirty and non-repeatable reads.
Serializable: Highest isolation in order to prevent phantom reads.
Snapshot: Maintains versioned data to avoid locking.
These levels balance between data consistency and performance in SQL

34. What is SQL Server Integration Services (SSIS)?
SQL Server Integration Services (SSIS) is a platform developed by Microsoft to carry out ETL (Extract, Transform, Load) functions. It generally allows data migration, transformation, and workflow automation across various data sources. Typically, SSIS is very useful for building data warehouses, which makes it essential for Business Intelligence(BI) projects.

35. What are the applications of SQL?
SQL is a popular language in various sectors and career roles. Its most important applications are:

Handling and searching in relational databases
Carrying out data analysis and generating reports
Creating backend logic in apps
Helping ETL pipelines in data warehousing
Maintaining data integrity and setting up access control
SQL flexibility turns it into a fundamental skill that data analysts, software developers, DBAs, and BI professionals all have in common.

36. What are SQL dialects?
SQL dialects are generally the variations of standard SQL syntax and features that are implemented by different database vendors. Examples include:

T-SQL for Microsoft SQL Server
PL/SQL for Oracle
pgSQL for PostgreSQL
MySQL’s extended SQL
Though the main SQL syntax is still fairly the same, these dialects bring in proprietary functions, procedural abilities, and performance features that are designed specifically for particular systems.

37. What are the different types of SQL operators?
SQL supports several operator categories:

Arithmetic Operators: +, -, *, / (perform calculations)
Comparison Operators: =, <, >, <=, >=, <> (used in WHERE clauses)
Logical Operators: AND, OR, NOT (combine multiple conditions)
Set Operators: UNION, INTERSECT, EXCEPT (combine result sets)
Understanding how to use these operators is crucial for writing efficient and readable SQL queries.

38. How to select all columns from a table?
In SQL, to get all the columns from a table, you can use the wildcard character asterisk (*)

SELECT * FROM table_name;
The above query retrieves all the columns of a table. Although it is a good practice during development, in production, it is advisable to explicitly mention the columns to be retrieved so as to increase performance and readability.

39. What are scalar functions in SQL?
Scalar functions in SQL are built-in functions that take one or more inputs and return a single value. Some of the common Scalar functions.

UPPER() / LOWER() – Converts text to uppercase or lowercase, respectively
LEN() – Returns the number of characters in a string
ROUND() – Rounds a numeric value to the specified number of decimal places
GETDATE() – Retrieves the current system date and time
These functions are useful for data formatting, transformation, and validation within SQL queries.

40. What is the difference between SQL and PL/SQL?
SQL is a declarative language that is used for defining as well as manipulating data in relational databases. It is mainly used for writing queries, inserting records, and managing the schema. Meanwhile, PL/SQL (Procedural Language/SQL) is Oracle’s extension to SQL that permits procedural features such as variables, loops, and conditional statements.

Although SQL is centered on data operations, PL/SQL is intended for programming logic and stored procedures; thus, it is more appropriate for the development of complicated business logic within Oracle databases.

41. What is the difference between on-premise SQL and cloud SQL?
On-premise SQL databases are installed on local servers, and internal teams take care of their maintenance, whereas cloud SQL services operate on cloud platforms such as AWS RDS, Google Cloud SQL, or Azure SQL, and the providers take care of management for them.

Criteria On-Premise SQL Cloud SQL
Infrastructure Local servers Cloud-managed infrastructure
Scalability Limited and manual Seamless and elastic
Maintenance Handled in-house Managed by the cloud provider
Cost Model Upfront hardware + licensing costs Pay-as-you-go pricing
42. Name two advantages of using cloud SQL services.

The two advantages of using cloud SQL services are:

High Availability and Automatic Backups: Cloud SQL services generally offer built-in redundancy, failover, and automated backups in order to ensure better reliability without manual effort.
Scalability and Cost Efficiency: With the cloud SQL service, you can easily scale storage and compute resources as needed and pay only for what you use, which simply reduces the overall infrastructure costs.
SQL Interview Questions for Experienced (3- 5 Years)
Now, with this section, we have listed the top SQL interview questions and answers for experienced professionals that will help you to prepare for mid to senior-level roles.

43. Explain the concept of database partitioning and its benefits.
Database partitioning divides a large table into smaller segments based on a chosen key. This improves the performance of the SQL queries by allowing queries to run on the specific partitions and reducing I/O operations.

44. What third-party tools are used in SQL Server?
The following is the list of third-party tools that are used in SQL Server:

SQL CHECK
SQL DOC 2
SQL Backup 5
SQL Prompt
Litespeed 5.0
45. What is SQL JOIN?
The SQL JOIN component joins rows from one or more tables in a relational database. Create sets that can be stored in tabular form or used routinely. JOIN is to combine columns from one table or multiple tables using the same value.

46. What is the difference between INNER JOIN and SELF JOIN?
The most important difference between INNER and SELF JOIN is:

INNER JOIN is used to return the records that are present in both tables. In contrast, a self-join is a type of INNER JOIN where a table is joined with itself.

47. Explain the difference between horizontal and vertical partitioning.
Horizontal: Splits a table by rows (e.g., by date ranges)

Vertical: Splits a table by columns (e.g., separating frequently vs rarely accessed fields)
Use horizontal for distributed querying, vertical for security/performance optimization.

48. What is the difference between the RIGHT JOIN and the LEFT JOIN?
Both RIGHT JOIN and LEFT JOIN do the same thing: They return the result of a query that contains all the records in the table. The only difference is that the LEFT JOIN returns all the records from the left table of the query, whereas the RIGHT JOIN returns all the records from the right table.

49. Is SELF JOIN an INNER JOIN or OUTER JOIN?
The SELF JOIN can be an INNER JOIN, OUTER JOIN, or a CROSS JOIN. SELF JOIN is used to link tables automatically based on columns that contain duplicate data in multiple rows.

50. What is the difference between a FULL JOIN and a CARTESIAN JOIN?
The combination of the LEFT and the RIGHT OUTER JOIN is called a FULL JOIN. If the ON condition cannot be satisfied, it returns all rows in both tables that match the WHERE clause with a NULL value. Whereas, a CARTESIAN or CROSS JOIN creates a cross-product between the two tables. For all rows, it returns a possible sequence.

51. What is NATURAL JOIN?
A NATURAL JOIN in SQL is a kind of join that automatically combines two tables only by the common columns that have the same name and compatible data types. Unlike INNER JOIN or EQUI JOIN, a NATURAL JOIN doesn’t require an explicit join condition using the ON clause.

It implicitly matches columns with identical names in both tables and returns rows where the values in those columns are equal.

52. What is an EQUI JOIN?
An EQUI JOIN is a type of join operation in a database that combines rows from two or more tables based on a matching condition using the equality operator (=). It is used to retrieve data where values in specified columns are equal.

Here is an example of the syntax for an EQUI JOIN:

SELECT column_name(s)
FROM table1
JOIN table2

-- Matches rows where values in the specified columns are equal
ON table1.column_name = table2.column_name.
53. Can you join a table to itself in SQL?
Yes, in SQL, it is possible to join a table to itself, which is known as a self-join. By using table aliases, you can treat the same table as two separate entities and perform a join operation on them based on specified conditions. Self-joins are used when you need to retrieve information by comparing rows within the same table.

54. How are JOINs different from the UNION clause?
A JOIN can be used if two tables share at least one attribute. The length of the retrieved rows is greater than the length of the rows in the corresponding tables.

Whereas in the case of UNION, a JOIN can be used if the query has the same number of columns and the corresponding attributes are the same. The number of rows returned is greater than the number of rows in each table in the query.

55. How would you track changes to sensitive data for auditing?
-- Create a table named 'audit_log' to track changes in data
CREATE TABLE audit_log (
  change_time TIMESTAMP,     -- Timestamp of when the change occurred
  user_id INT,     -- Id of the user who made the change
  old_value JSONB,     -- Previous state of the data stored as JSONB
  new_value JSONB     -- Updated state of the data stored as JSONB
);
Use triggers or CDC (Change Data Capture) to populate this table.
56. What is a HASH JOIN?
A HASH JOIN requires two inputs, an INNER table and an OUTER table. HASH JOINS involve using a HASH table to identify matching rows between two tables. HASH JOINS are an option when other joins are not recommended. When joining large data sets that are unsorted or non-indexed, HASH JOINS are better.

57. What is MERGE JOIN?
MERGE JOIN is one of the most important join types in SQL Server. In MERGE JOIN, your query plan is effective, and you don’t need to make many changes to improve query performance because the MERGE JOIN operator uses ordered data entry, it can use two large data sets.

58. Can you explain NESTED JOIN in SQL?
In SQL, a Nested Join (also referred to as a Nested Loop Join) is the basic method that most relational databases employ for connecting two tables. It is the default approach that database engines frequently use for joining small or medium datasets.

In a Nested Join, one table is treated as the outer table, and for each row in this outer table, the system searches for matching rows in the inner table. This process repeats until all matching combinations are found.

59. Explain Common Table Expressions in SQL.
In general, a Common Table Expressions (CTEs) is a temporary, named result set that can be used to refer to an UPDATE, INSERT, SELECT, or DELETE statement. A CTE can be specified by adding WITH before an UPDATE, INSERT, DELETE, SELECT, or MERGE statement. Multiple CTEs can be used in the WITH clause by separating them with commas.

60. What is a recursive CTE?
A recursive CTE (Common Table Expression) is a SQL construct that enables a query to refer to itself in order to carry out iterative tasks. Generally, it is used to handle hierarchical or tree-like data, such as employee-management hierarchies or category-subcategory structure

Example syntax:

WITH RECURSIVE employee_hierarchy AS (
    SELECT id, name, manager_id
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy;
Understand how hierarchical recursive queries work in MySQL through this blog.

61. How will you structure data to perform a JOIN Operation in a one-to-many relationship situation?
To create a one-to-many relationship, you need to add the primary key from one side to many sides as a column. To create a many-to-many relationship, you need a middle table that contains the primary keys from the many-to-many tables.

SQL Query Interview Questions and Answers
In this section, we’ve covered essential SQL query interview questions and answers that are crucial for demonstrating your practical SQL skills in technical interviews. These SQL coding questions will help you tackle complex data challenges with confidence in your next interview.

62. Write an SQL syntax for joining 3 tables.
select tab1.col1, tab2.col2,tab3.col3 (columns to display) from table1
Join     -- Any type of join
table2 on tab1.col1 = tab2.col1     -- Any matching columns
Join     -- Any type of join
table3 on tab 2.col1 = tab 3.col1     -- Any matching columns
63. Write a query to select specific columns, say name and age, from a table called Employees.
SELECT name, age     -- Select specific columns
FROM Intellipaat_Emp;     -- Table name
64. Write a query to get employees older than 35 and working in the operations department.
SELECT *
FROM Intellipaat_Emp     -- Table name
WHERE age > 35     -- Age is greater than 35
AND department = 'operation';
65. Write a query to find the average salary for each department.
SELECT
department,
AVG(salary) AS avg_salary     -- Calculate the average salary
FROM
Intellipaat_Emp
GROUP BY
department;     -- Group the results by department to get one average per group
66. Write a query to find employees whose names start with ‘Int’.
SELECT *
FROM employees

-- Filter rows where the employee name starts with 'Int'
WHERE employee_name LIKE 'Int%';
67. Write a query to add a new employee record.
INSERT INTO Intellipaat_Emp (name, age, department, salary)
VALUES ('John Doe', 28, 'Marketing', 50000);
68. Write a query to retrieve the last five records from the Employees table based on the ID column.
SELECT * FROM Intellipaat_Emp

-- Order the results by 'id' in descending order

ORDER BY id DESC

-- Return only the top 5 rows

LIMIT 5;
69. Write a query to label employees with salaries above 5000 as “High Salary.”
SELECT name,
salary,
CASE     -- Use CASE to create a new column 'salary_category' based on salary value

-- If salary is greater than 5000, label as 'High Salary'
WHEN salary > 5000 THEN 'High Salary'
ELSE 'Low Salary'     -- Otherwise label as ‘Low Salary’
END AS salary_category     -- Name the resulting column as 'salary_category'
FROM Intellipaat_Emp
70. Write a query to get all employees and their project names, showing NULL if an employee is not assigned a project.
SELECT Employees. name,Projects.project_name
FROM Intellipaat_Emp AS Employees
LEFT JOIN Projects     -- Use LEFT JOIN to include all employees
ON Employees.project_id = Projects.id;
71. Write an SQL query to display each department along with the name of any employee who works in that department. If a department has no employees, show the department with NULL for the employee’s name.
SELECT dept.DepartmentName,int_emp.Name
FROM Employees AS int_emp
RIGHT JOIN Departments AS dept     -- Use RIGHT JOIN to include all departments
ON int_emp.DepartmentID = dept.DepartmentID;
72. Write a query to increase the salary of all employees in the ‘HR’ department by 10%.
UPDATE Intellipaat_Emp
SET salary = salary * 1.1     -- Increase salary by 10% (multiply by 1.1)
WHERE department = 'HR';     -- Apply this change to employees in the 'HR' department
73. Write a query to fetch unique employee names where duplicate names exist in the Employees table.
SELECT name
FROM Intellipaat_Emp
GROUP BY name
HAVING COUNT(*) = 1;
74. Find all duplicate rows in the table Employees, considering all columns.
SELECT *
FROM Intellipaat_Emp
GROUP BY name, age, department, salary     -- Group by all columns to detect identical rows
HAVING COUNT(*) > 1;     -- Only include duplicate groups.
75. How will you calculate the total sales in each category of a product sales table?
To calculate the total sales in each category of a product sales table, we can use the aggregate function (SUM) with the sales amount column and group it by the category column.

SELECT category,
SUM(sales_amt) AS Total_Sales     -- Calculate total sales amount per category and name the result as 'Total_Sales'
FROM sales
GROUP BY category;     -- Group results by category to get totals for each one
76. How can you copy data from one table to another table?
--We can use the INSERT INTO SELECT operator.
INSERT INTO employee_duplicate
SELECT *
FROM employees;
77. Write a query to fetch employees who earn more than the average salary.
SELECT*
FROM Intellipaat_Emp

-- Compare each employee's salary to the average salary
WHERE salary > (SELECT AVG(salary)
FROM Intellipaat_Emp);
78. How would you find the 2nd-highest salary from a table called Employees?
SELECT MAX(salary)     -- Filter out the top salary
FROM Intellipaat_Emp
WHERE salary < (SELECT MAX(salary)     -- Filter out the top salary
FROM Intellipaat_Emp);
For the Nth highest salary, replace MAX with LIMIT:

SELECT DISTINCT salary
FROM Intellipaat_Emp
ORDER BY salary DESC     -- Sort salaries from highest to lowest
LIMIT N-1, 1;     -- Skip the top (N-1) salaries and return the Nth highest one
79. Write a query to select only even or odd rows from a table based on an ID field.
-- Even rows
SELECT *
FROM Intellipaat_Emp
WHERE id % 2 = 0;     -- IDs divisible by 2 are even

-- Odd rows
SELECT *
FROM Intellipaat_Emp
WHERE id % 2 = 1;
80. Write a query to select the top 2 salaries from each department in the Employees table.
SELECT*
FROM (
SELECT name, department, salary,
ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM Intellipaat_Emp
) AS ranked
WHERE rank <= 2;
81. If you have an ID column with sequential numbers but some values are missing, write a query to find the missing numbers.
SELECT id + 1 AS missing_id     -- Predict the next ID and label it as 'missing_id'
FROM Intellipaat_Emp
WHERE (id + 1) NOT IN (SELECT id FROM Intellipaat_Emp);     -- Check if the next ID is missing and get all existing IDs
82. Write a query to swap the values in a column, for example, changing all ‘Male’ to ‘Female’ and vice versa in the column gender.
UPDATE Intellipaat_Emp
SET gender = CASE
WHEN gender = 'Male' THEN 'Female'     -- If gender is 'Male', change it to 'Female'
ELSE 'Male'     -- Otherwise (Female), change to 'Male'
END;
83. Write a query to find pairs of employees who have the same salary.
SELECT A.name AS employee1, B.name AS employee2, A.salary
FROM Intellipaat_Emp A

-- Self-join and Match employees with the same salary.
JOIN Intellipaat_Emp B ON A.salary = B.salary
AND A.name < B.name;     -- Avoid duplicate pairs and self-matches
84. Write a query to find the number of days an employee has been with the company.
-- Difference in days between today and joining date
SELECT name, DATEDIFF(CURDATE(), joining_date)
AS days_with_company
FROM Intellipaat_Emp;
85. Find pairs of employees who were hired on the same day.
SELECT A.name AS employee1, B.name AS employee2, A.joining_date
FROM Intellipaat_Emp A, Employees B
WHERE A.joining_date = B.joining_date
AND A.name < B.name;     -- Avoid duplicate and pair
86. Write a query to find the median salary in each department from the Employee table.
Hint: You may use ROW_NUMBER() or PERCENT_RANK() to determine median values.

WITH RankedSalaries AS (
SELECT department, salary,

-- Ascending rank
ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary) AS rn_asc,

-- Descending rank
ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn_desc
FROM Intellipaat_Emp
)
SELECT department, AVG(salary) AS median_salary
FROM RankedSalaries
WHERE rn_asc = rn_desc OR rn_asc + 1 = rn_desc
GROUP BY department;
87. Write a query to get the top 10% of employees by salary.
Hint: Use PERCENT_RANK() to filter out top percentages.

SELECT *
FROM (
SELECT name, salary,

-- Rank employees by descending salary
PERCENT_RANK() OVER (ORDER BY salary DESC) AS pct_rank
FROM Intellipaat_Emp
) AS Ranked
WHERE pct_rank <= 0.1;     -- Select only the top 10%
88. Write a query to calculate the cumulative salary (running total) within each department.
SELECT department, name, salary,
SUM(salary) OVER
(PARTITION BY department     -- Restart the running total for each department
 ORDER BY name     -- Running total is ordered by employee name
) AS cumulative_salary
FROM Intellipaat_Emp;
89. Write a query to calculate the time gap (in hours) between consecutive logins for each user.
SELECT user_id, login_time,
TIMESTAMPDIFF(HOUR,
LAG(login_time) OVER (
PARTITION BY user_id     -- Reset tracking for each user
 ORDER BY login_time),     -- Compare each login with the previous one chronologically
login_time)     -- Current login time
 AS hours_since_last_login
FROM Logins;

### 90. Write a query to get a full list of products, including products that have no sales, by performing a full outer join between product_dim and sales_fact

```sql
SELECT p.product_id, p.product_name, SUM(s.sale_amount) AS total_sales
FROM product_dim p
LEFT JOIN sales_fact s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name

UNION

-- Set sales to 0 explicitly for products with no sales
SELECT p.product_id, p.product_name, 0 AS total_sales
FROM product_dim p
WHERE NOT EXISTS (
SELECT 1
FROM sales_fact s

-- Check if the product exists in the sales table
WHERE p.product_id = s.product_id  
);
```

### 91. Write a query to calculate the year-to-date (YTD) sales for each product up to the current date in the sales_fact table

```sql
SELECT product_id,
SUM(sale_amount) OVER (PARTITION BY product_id
ORDER BY sale_date
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS ytd_sales
FROM sales_fact
WHERE sale_date <= CURRENT_DATE
ORDER BY product_id;
```

### 92. How would you find the second-highest salary from a table?

```sql
SELECT * FROM employee;
SELECT MAX(e_salary)
FROM employee
WHERE e_salary NOT IN (SELECT MAX(e_salary) FROM employee);
```

### 93. How will you fetch the most recent entries in a database?

We can fetch the most recent entries in a database by using the ORDER BY clause along with the timestamp column in descending order.

```sql
SELECT *
FROM table_name
ORDER BY timestamp_column DESC;     -- Sort by timestamp in descending order
```

94. How will you find the IDs or details where there have been no entries in terms of sales?
To find the IDs or details where there have been no entries in terms of sales, we can use the LEFT JOIN or NOT EXISTS clause.

Assume we have two tables: product with product details and sales with sales data.

Left Joins:

```sql
SELECT p.product_id, p.product_name
FROM product p
LEFT JOIN sales s ON p.product_id = s.product_id
WHERE s.product_id IS NULL;
```

Here, the WHERE s.product_id is NULL condition helps us filter out the rows where a match in the sales table is not found.

Not Exists:

```sql

SELECT p.product_id, p.product_name
FROM products p
WHERE NOT EXISTS (
SELECT 1
FROM sales s
WHERE s.product_id = p.product_id
);
```

### 95. Suppose there is a database where information about the employees in various verticals is stored. Your task is to find the average salary of each vertical and the highest salary among the lot

To find the average salary of each vertical and the highest salary among the employees, we can use the group by clause along with the aggregate functions (AVG and MAX).

```sql

SELECT vertical,     -- Grouping by vertical
AVG(salary) AS average_salary,     -- Calculate average salary for each vertical
MAX(salary) AS highest_salary     -- Find the highest salary in each vertical
FROM employees
GROUP BY vertical;     -- Group the results by vertical
Where,
```

vertical: column that you want to group
salary: column in the table
employees: table name

### 96. Given data on where the store inventory is stored, your task is to find the top 3 products in each category in terms of price

To find the top 3 products in each category in terms of price, we can group by clause along with the aggregate function (MAX) with the price column, and set the limit as 3 in descending order.

```sql
SELECT category,
product_name,
MAX(price) AS max_price
FROM inventory
GROUP BY category, product_name
ORDER BY category, max_price DESC
LIMIT 3;
```

### 97. Write an SQL query to find the month-on-month sales of a specific product in a store

To calculate the month-on-month sales of a specific product in a store, we can use a combination of date functions and aggregate functions.

— Extract year and month from the sale date

```sql
SELECT EXTRACT(YEAR_MONTH FROM sale_date) AS year_month,
SUM(quantity_sold) AS total_sales     -- Calculate total quantity sold for each month
FROM sales
WHERE product_id = 'your_product_id'     -- Filter by the specific product
GROUP BY year_month     -- Group data by year and month
ORDER BY year_month;     -- Sort results by year and month
```

## 98. Suppose in an organisation, employees are mapped under managers. Write an SQL query that will fetch you the managers and employees working under them

To fetch the managers and employees working under them, we can use a self-join to fetch the managers and the employees working under them.

```sql
SELECT M.manager_id AS manager_id,     -- Manager's ID
M.manager_name AS manager_name,     -- Manager's name
E.employee_id AS employee_id,     -- Employee's ID
E.employee_name AS employee_name     -- Employee's name
FROM employees E
JOIN employees M ON E.manager_id = M.employee_id
ORDER BY M.manager_id, E.employee_id;     -- Sort by manager ID first, Then sort by employee ID
```

### 99. In a store inventory, your task is to fetch the total quantity of the top product purchased by the customers

To fetch the total quantity of the top product purchased by the customers, we can use a group by clause along with the limit in descending order.

```sql
SELECT product_id,

-- Calculate total quantity purchased for each product
SUM(quantity_purchased) AS total_quantity_purchased
FROM purchases
GROUP BY product_id     -- Group the data by product to aggregate purchase quantities
ORDER BY total_quantity_purchased DESC     -- Sort in descending order
LIMIT 1;     -- Return the top product
```

### 100. You need to create a materialised view to store the monthly total sales by product for faster reporting. Write the SQL to create this view

CREATE MATERIALIZED VIEW mv_monthly_sales AS

```sql
SELECT
product_id,
YEAR(sale_date) AS year,     -- Extract the year from sale_date
MONTH(sale_date) AS month,     -- Extract the month from sale_date
SUM(sale_amount) AS total_sales     -- Total sales amount per product per month
FROM sales_fact

-- Grouping to get monthly totals
GROUP BY product_id, YEAR(sale_date), MONTH(sale_date);
```

### 101. Write a query that detects missing dates in a sequence from a sales table. The sales table contains sale_date and sale_amount, and you need to find any missing dates between the earliest and latest sales dates

```sql
WITH DateSeries AS (

-- Earliest date in the sales table , latest date in the sales table
SELECT MIN(sale_date) AS start_date, MAX(sale_date) AS end_date
FROM sales
)

-- Generate date by adding seq days to start_date
SELECT DATE_ADD(start_date, INTERVAL seq DAY) AS missing_date
FROM DateSeries,
(SELECT @rownum := @rownum + 1 AS seq
FROM sales,
(SELECT @rownum := 0) AS r) AS seq_numbers     -- Initialize row number

-- Ensure the generated date is within the range
WHERE DATE_ADD(start_date, INTERVAL seq DAY) <= end_date
AND DATE_ADD(start_date, INTERVAL seq DAY) NOT IN (SELECT sale_date FROM sales)
ORDER BY missing_date;
```

### 102. You have an order table with millions of rows, and you frequently run a query that filters it by customer_id, order_date, and status. What indexes would you create to optimize this query, and why?

We need to create a composite index on columns that are frequently used for filtering.

```sql
CREATE INDEX idx_orders_customer_date_status
ON orders (customer_id, order_date, status);
```

103. Write a query using a Common Table Expression (CTE) to rank customers by total purchase amount and return the top 10 customers.

```sql
WITH RankedCustomers AS (
-- Calculate total purchases for each customer
SELECT customer_id, SUM(purchase_amount) AS total_spent,

--Rank customers by spending (highest first)
RANK() OVER (ORDER BY SUM(purchase_amount) DESC) AS rank
FROM orders
GROUP BY customer_id     -- Group by customer id
)
SELECT customer_id, total_spent
FROM RankedCustomers
WHERE rank <= 10;     -- Filter to return only top 10 ranked customers
```

### 104. Can you identify the employee who has the third-highest salary from the given employee table (with salary-related data)?

Consider the following employee table. In the table, Sabid has the third-highest salary (60,000).

Name Salary
Tarun 70,000
Sabid 60,000
Adarsh 30,000
Vaibhav 80,000
Below is a simple query to find out which employee has the third-highest salary. The functions RANK, DENSE RANK, and ROW NUMBER are used to obtain the increasing integer value by imposing the ORDER BY clause in the SELECT statement, based on the ordering of the rows. The ORDER BY clause is necessary when the RANK, DENSE RANK, or ROW NUMBER functions are used. On the other hand, the PARTITION BY clause is optional.

```sql
WITH CTE AS
(
SELECT Name, Salary, ROW_NUMBER() OVER (ORDER BY Salary DESC) AS RN
FROM EMPLOYEE
)
SELECT Name, Salary
FROM CTE
WHERE RN = 3;
```

### 105. Create tables- Customer details and Product details

So, based on these two tables, let’s look into some of the questions related to SQL JOINS and queries.

### 106. What is the difference between NULL, 0, and an empty string (“”)?

NULL = Unknown or missing value
0 = Numeric value
"" = Empty string (text)

### 107. Get the customer name and product name ordered by first name from the customer

```sql
SELECT first_name, b.Product_name FROM [customer] A
LEFT OUTER JOIN [Product] B     -- Left join to include customers without orders
ON A.customer_id = B.customer_id     -- Join condition on customer_id
ORDER BY a.first_name     -- Order the result by customer's first name
```

### 108. Get the customer’s name and the product name ordered by first name

```sql
SELECT a.First_Name, ISNULL(b.Product_name,'-No Project Assigned') AS Product_Name
FROM customer A LEFT OUTER JOIN product B
ON A.customer_id = B.customer_id ORDER BY a.first_name
```

### 109. Get all product names even if they have not matched any customer ID, in the left table, order by first name

```sql
SELECT a.first_name,b.Product_name
FROM [customer] A RIGHT OUTER JOIN [product] B
ON a.customer_id = b.customer_id ORDER BY a.first_name
```

### 110. Get the complete record (customer name, product name) from both tables ([CustomerDetail], [ProductDetail]); if no match is found in any table, then show NULL

```sql
SELECT a.first_name,b.Product_name FROM [customer] A
FULL OUTER JOIN [product] B
ON a.customer_id = b.customer_id
ORDER BY a.first_name
```

### 111. Write a query to find out the product name that is not assigned to any employee( tables: [CustomerDetail],[ProductDetail])

```sql
SELECT b.Product_name FROM [customer] A
RIGHT OUTER JOIN [product] B
ON a.customer_id = b.customer_id
WHERE a.first_name IS NULL
```

### 112. Explain the CAP Theorem

CAP Theorem, also known as Brewer’s Theorem, which is a key concept in distributed systems that states all three properties cannot be guaranteed at the same time:

Consistency
Availability
Partition Tolerance
*The output will not come as there is no duplicate record in the product table.

### 113. Write down the query to fetch the ProductName on which more than one customer is working, along with the CustomerName

```sql
Select P.Product_name, c.first_name from product P INNER JOIN customer c
on p.customer_id = c.customer_id
where P.Product_name in(select Product_name from product group by Product_name having COUNT(1)>1)
```

*The output will not come as there is no duplicate record in the product table.

### 114. What is DESC in SQL?

In SQL, DESC stands for descending. It is used to sort records in descending order, i.e., highest to lowest. It is usually clubbed with the ORDER BY clause to sort records. Here is an example of the same:

```sql
SELECT * FROM employees ORDER BY salary DESC;
```

### 115. What is a schema in SQL?

In SQL, a schema can be termed as a structure that groups tables, views, databases, and stored procedures. Using a schema prevents conflict and allows two names to exist in parallel, divided by the schema. Here is an example of the same:

```sql
CREATE SCHEMA sales;
CREATE TABLE sales.orders (
order_id INT,
order_date DATE
);
```

### 116. Can we rollback DELETE?

Yes, after using the DELETE command, you can roll back if you are using the TRANSACTION command. DELETE is a DML command, so when you rollback, all the transactions are undone and the records are restored. Here is an example of the same:

```sql
BEGIN TRANSACTION;     -- Begin a transaction block
DELETE FROM employees
WHERE employee_id = 101;     -- Delete the employee with ID 101
ROLLBACK;     -- Roll back the transaction (undo the delete operation)
```

### 117. Explain how CASE statements work in SQL

CASE provides if-then-else logic in SQL like this:

```sql
SELECT product_name,
CASE WHEN price > 100 THEN 'Premium'
WHEN price > 50 THEN 'Standard'
ELSE 'Budget' END AS tier
FROM products
```

### 118. What is a pivot in SQL?

The PIVOT command is used to summarise the data. It converts rows into columns, which helps in better analysis. Let’s understand this using an example:

Input Data:

Product Year Sales
A 2022 100
B 2022 150
A 2023 200
B 2023 250
Question: Find the sales of Product A and Product B in 2022 and 2023

Output Data:

```sh
Product sales_2022 sales_2023
A 100 200
B 150 250
```

Query Used:

```sql
SELECT product, [2022] AS sales_2022, [2023] AS sales_2023
FROM (
SELECT product, year, sales
FROM sales
) AS SourceTable
PIVOT (
SUM(sales)
FOR year IN ([2022], [2023])
) AS PivotTable;
```

119. What is a dynamic SQL query?
A Dynamic SQL query is a technique in SQL wherein the query is built during runtime, giving dynamic inputs in the query. This makes the query flexible enough to create multiple use cases using the same query. Here is an example of the same:

DECLARE @tableName NVARCHAR(50) = 'employees';
DECLARE @query NVARCHAR(MAX);
SET @query = 'SELECT * FROM ' + @tableName + ' WHERE department = ''HR''';
EXEC(@query);
