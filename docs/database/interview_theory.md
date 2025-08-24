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
