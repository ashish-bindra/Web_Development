# SQL FAQ

## 1. Integrity constraints

It can be called as a declarative way in order to define a business rule for a table's cloumn.

## 2. Index

- It can be called as an optional strucure which is associalted with a table for direct access to the rows.
- Index can be created for one or more columns in table.

## 3. Extent

- It can be defined as a specific number of contigous data blocks in single allocation
- it is used to store a specific type of information

## 4. List the type of joins used in writing SUBQUeries

- Self Join
- Outer JOIN
- equi-join

## 5. List the various Oracle database objects

- Table
- views
- indexes
- Synonyms
- Squences
- TablesAces

## 6 Tell about to use of

1. Rename
2. Alias

- Rename:
  - It is a permanent name provide to a table or column.

- Alias:
  - It is tempory name provide to a table or column which get over after the execution of SQL statement

## 7. What is View?

- It is virtual table which is defined as a stored procedure based on one or more tables.

## 8. What are various components of physical databases strucure of oracle database

- Oracle database components of three of files

1. Data Files
2. Redo logo files
3. control files

## 9. List out components of logocal database strucures of oracle database

- Table spaces
- Database is schema object

## 10. What do you mean by a tablespace?

- THere are logical storeage units into which a database dicied.
- It is used to group togather the related logical strucure.

## 11. What is a synonyms? What are its various types?

- A Synonym can be called as an alias for a table, view,squence or program unit.it is basically of two types.
- private: Only the owner can access it.
- Public: can be accessed by any database user

## 12. What are uses of synonyms?

- Mask the real name and owner of an object
- Provide public access to an object
- provide location transparcing for table view or program unit of a remote database.
- Siplify the SQL statements for database users

## 13. What do you mean by a deadlock?

- When two processes are waiting to update the rows of datable which are locked by another process the sitwation as called deadlock
The resion of it to happen are:
- Lack of proper row lock commands
- Poor design of frontend application
0 It reduces the performances of the server servely
- There locks get automatically released automatically when a commit/rollback operation is perform or any process is killed externally