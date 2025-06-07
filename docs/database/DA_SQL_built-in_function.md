# Hands-on Lab: Built-in functions - Aggregate, Scalar, String, Date and Time Functions

    ID ANIMAL QUANTITY COST RESCUEDATE
    1 Cat 9 450.09 5/29/2018
    2 Dog 3 666.66 6/1/2018
    3 Dog 1 100 6/4/2018
    4 Parrot 2 50 6/4/2018
    5 Dog 1 75.75 6/10/2018
    6 Hamster 6 60.6 6/11/2018
    7 Cat 1 44.44 6/11/2018
    8 Goldfish 24 48.48 6/14/2018
    9 Dog 2 222.22 6/15/2018

## After completing this lab, you will be able to

Compose and run sub-queries with multiple tables
Check query results and view log files

%load_ext sql

The sql extension is already loaded. To reload it, use:
  %reload_ext sql

%sql sqlite:///PETRESCUE-CREATE.db

## Exercise 2: Aggregate Functions

### Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.

```sql
%%sql
select * from PETRESCUE 
```



Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.

Query A3: Enter a function that displays the maximum quantity of animals rescued.

Query A4: Enter a function that displays the average cost of animals rescued.

Query A5: Enter a function that displays the average cost of rescuing a dog.

#### Exercise 3: Scalar and String Functions
Query B1: Enter a function that displays the rounded cost of each rescue.

Query B2: Enter a function that displays the length of each animal name.

Query B3: Enter a function that displays the animal name in each rescue in uppercase.

Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.

Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.

#### Exercise 4: Date and Time Functions
Query C1: Enter a function that displays the day of the month when cats have been rescued.

Query C2: Enter a function that displays the number of rescues on the 5th month.

Query C3: Enter a function that displays the number of rescues on the 14th day of the month.

Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.

Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between todays date and the rescue date.


#### Lab Solutions
Exercise 2 Solutions: Aggregate Functions
Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.

select SUM(COST) from PETRESCUE;

Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.

select SUM(COST) AS SUM_OF_COST from PETRESCUE;

Query A3: Enter a function that displays the maximum quantity of animals rescued.

select MAX(QUANTITY) from PETRESCUE;

Query A4: Enter a function that displays the average cost of animals rescued.

select AVG(COST) from PETRESCUE;

Query A5: Enter a function that displays the average cost of rescuing a dog.

Hint - Bear the cost of rescuing one dog on one day, which is different from another day. So you will have to use an average of averages.

select AVG(COST/QUANTITY) from PETRESCUE where ANIMAL = 'Dog';

Exercise 3 Solutions: Scalar and String Functions
Query B1: Enter a function that displays the rounded cost of each rescue.

select ROUND(COST) from PETRESCUE;

Query B2: Enter a function that displays the length of each animal name.

select LENGTH(ANIMAL) from PETRESCUE;

Query B3: Enter a function that displays the animal name in each rescue in uppercase.

select UCASE(ANIMAL) from PETRESCUE;

Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.

`select DISTINCT(UCASE(ANIMAL)) from PETRESCUE;

Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.

select * from PETRESCUE where LCASE(ANIMAL) = 'cat';

Exercise 4 Solutions: Date and Time Functions
Query C1: Enter a function that displays the day of the month when cats have been rescued.

select DAY(RESCUEDATE) from PETRESCUE where ANIMAL = 'Cat';

Query C2: Enter a function that displays the number of rescues on the 5th month.

select SUM(QUANTITY) from PETRESCUE where MONTH(RESCUEDATE)='05';

Query C3: Enter a function that displays the number of rescues on the 14th day of the month.

select SUM(QUANTITY) from PETRESCUE where DAY(RESCUEDATE)='14';

Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.

select (RESCUEDATE + 3 DAYS) from PETRESCUE;

Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between todays date and the rescue date.

select (CURRENT DATE - RESCUEDATE) from PETRESCUE;