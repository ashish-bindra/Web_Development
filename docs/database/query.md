# Practice queries

<https://www.programiz.com/sql/online-compiler/>

![alt text](<img/avalable tables.PNG>)

## Q 1: FIND TOTAL COUNT OF CUSTOMER ID IN TABLE CUSTOMER?

ANS: `SELECT COUNT (CUSTOMER_id) AS TOTAL_COUNT FROM CUSTOMERS`

![1.PNG](img/1.PNG)

## QUE 2:FIND TOTAL Customers WHERE AGE IS GREATOR THAN 23?

```sql
SELECT COUNT (CUSTOMER_id) AS TOTAL_COUNT FROM CUSTOMERS WHERE AGE > '23'
```

![2.PNG](img/2.PNG)

## Q3: COUNT LIST OF RECORD WHERE COUNTRY nane IS USA?

```sql
SELECT COUNT (COUNTRY) AS TOTAL_RECORD FROM CUSTOMERS WHERE 
COUNTRY='USA'
```

![3.PNG](img/3.PNG)

## Q4: COUNT LIST OF RECORD WHERE FIRST NAME STARTS WITH J?

```sql
SELECT COUNT (FIRST_NAME) AS NAMES FROM CUSTOMERS WHERE FIRST_NAME LIKE 'J%'
```

![4.PNG](img/4.PNG)

## Q5: FETCH COUNT NUMBER RECORD OF CUSTOMERS WHERE AGE LIMIT BETWEEN 20 TO 28?

```sql
SELECT COUNT (customer_id) FROM CUSTOMERS WHERE AGE BETWEEN '25' AND '28'
```

![5.PNG](img/5.PNG)

## Q5: FETCH COUNT NUMBER RECORD OF CUSTOMERS WHERE  not AGE LIMIT BETWEEN 20 TO 28?

![5.5.PNG](img/5.5.PNG)

## Q6: FIND HIHGEST AGE IN CUSTOMER?

```sql
SELECT MAX (AGE) AS HIGH_AGE FROM CUSTOMERS
```

![6.PNG](img/6.PNG)

## Q7: FIND MIN AGE IN CUSTOMER?

```sql
SELECT MIN (AGE) AS LOW_AGE FROM CUSTOMERS
```

![7.PNG](img/7.PNG)

## Q8: FIND SECOND HIGHEST AGE IN CUSTOMER?

```sql
SELECT * FROM CUSTOMERS ORDER BY AGE DESC LIMIT 1,1
```

***NOTE : IT WILL SKIP THE FIRST VALUE AND SHOW SECOND VALUE LIKE ..AFTER SORTING***

***SECOND WAY:***

```sql
SELECT MAX(A.AGE) FROM CUSTOMERS A, CUSTOMERS S
WHERE A.AGE<S.AGE`
```

***BEST WAY:***

```sql
SELECT MAX(AGE) FROM CUSTOMERS WHERE AGE < (SELECT MAX(AGE) FROM CUSTOMERS)`
```

![8.PNG](img/8.PNG)

## Q9: Display customer details WHO CUSTOMERID IS 4 AND SHOW THE DETAILS FOR ALL THE CUSTOMERS WHO LIVES IN SAME COUNTRY?

```sql
SELECT * FROM CUSTOMERS WHERE COUNTRY=(SELECT COUNTRY FROM CUSTOMERS WHERE CUSTOMER_ID = '4')```
***BEST WAY :***
```sql
SELECT T2.* FROM Customers T1, customerS T2
WHERE T1.CUSTOMER_id = '4' AND T1.cOUNTRY = T2.cOUNTRY;
```

![9.PNG](img/9.PNG)

## Q10: Country wise highest AGE , LOWEST AGE?

```sql
SELECT MAX(AGE) FROM CUSTOMERS ORDER BY FIRST_NAME
SELECT MIN(AGE) FROM CUSTOMERS ORDER BY CUSTOMER_iD

SELECT country, MIN(AGE) AS lowest_age
FROM Customers
GROUP BY country;
```

![10.1.PNG](img/10.1.PNG)

---

![10.2.PNG](img/10.2.PNG)

## Q11: Counts No of CUSTOMERS in each COUNTRY or counts no of ITEMS in Each OrderID

```sql
SELECT country, COUNT(country) AS no_of_customer FROM customers GROUP BY  country
```

![11.PNG](img/11.PNG)

## Q12: Display Alternate Records(1,3,5 or 2,4,6) ?

```sql
SELECT * FROM CUSTOMERS WHERE CUSTOMER_ID%2=1 (FOR ODD)

SELECT * FROM CUSTOMERS WHERE CUSTOMER_ID%2!=1 (FOR EVEN)

```

Note:  The modulo operation on CUSTOMER_ID will not guarantee alternating records in the sequence of rows returned.
  
- Alternate records without usinf customerID

```sql
        WITH NumberedRows AS (
            SELECT *, ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS RowNum
            FROM Customers
            )
            SELECT *
            FROM NumberedRows
            WHERE RowNum % 2 = 1;
```

![12.PNG](img/12.PNG)

## Q13: SHOW FIRST_NAME AND LAST_NAME AND AGE BY DESC ORDER OF AGE

```sql
SELECT FIRST_NAME,LAST_NAME ,AGE FROM CUSTOMERS ORDER BY AGE DESC
```

![13.PNG](img/13.PNG)

## Q14 : Display Duplicate name of a Column

- (GROUP BY USING ALL DUPLICATE VALUES HAS BEEN REMOVED AND WE NEED TO SEARCH MORE ON IT)
- Select first_name from customers group by first_name

- Display Duplicate of a Column (NEED TO SEARCH MORE HAVING BY & GROUP BY)
  - `Select first_name,COUNT(*) from customers GROUP BY FIRST_NAME HAVING COUNT(*)>1;`

- OR (IF WE WANT TO PRINT THE FULL RECORD)

```sql
        SELECT *
        FROM CUSTOMERS
        WHERE FIRST_NAME IN (
            SELECT FIRST_NAME
            FROM CUSTOMERS
            GROUP BY FIRST_NAME
            HAVING COUNT(*) > 1
        );


        SELECT *
        FROM your_table
        WHERE column_name IN (
            SELECT column_name
            FROM your_table
            GROUP BY column_name
            HAVING COUNT(*) > 1
        );
```

![14.PNG](img/14.PNG)

## Q15: Select first 4 row from tabel

```sql
SELECT * FROM CUSTOMERS LIMIT 4
```

![15.PNG](img/15.PNG)

## Q16: JOINS TWO TABLE AND SHOW ALL COULUMS FOR BOTH THE TABLES AND PRINT LAST THREE LESSER AMOUNT

```sql

    SELECT * FROM CUSTOMERS
    JOIN ORDERS ON CUSTOMERS.CUSTOMER_ID = ORDERS.CUSTOMER_ID
     ORDER BY AMOUNT LIMIT 3;
```

NOTE : WE HAVE USE FULL JOIN HERE AND PRINT THE LOWEST THREE VALUES OF AMOUNT
![16.PNG](img/16.PNG)

## Q17: Print FIRST_NAME , LAST_NAME AND AMOUNT WHO BROUGHT KEYBOARD

```sql
    SELECT FIRST_NAME, LAST_NAME, AMOUNT
        FROM CUSTOMERS
        JOIN ORDERS ON CUSTOMERS.CUSTOMER_ID=ORDERS.CUSTOMER_ID
        WHERE ITEM LIKE '%KEYBOARD%
```

 ![17.PNG](img/17.PNG)

## Q18: PRINT LIST IF ITEM , PRICE WHICH IS SELLING IN USA OR UK

```sql
    SELECT ITEM,AMOUNT
    FROM CUSTOMERS
    JOIN ORDERS
    ON CUSTOMERS.CUSTOMER_ID=ORDERS.CUSTOMER_ID
    WHERE COUNTRY IN ('USA','UAE')
```

![18.PNG](img/18.PNG)

## Q 19: PRINT LIST IF ITEM , AMOUNT,COUNTRY WHICH HAS BEEN DELIVERED

- (JOINS FOR THREE TABLES)

```sql
    SELECT ITEM,AMOUNT,COUNTRY
    FROM CUSTOMERS
    JOIN ORDERS
    ON CUSTOMERS.CUSTOMER_ID=ORDERS.CUSTOMER_ID
    JOIN SHIPPINGS ON CUSTOMERs.CUSTOMER_ID=SHIPPINGS.CUSTOMER
    WHERE STATUS = 'Delivered'
```

![19.PNG](img/19.PNG)

## Q20 :  union vs uninonall

- UNION (REMOVE DUPLICATES)
  - Purpose: Combines the results of two or more queries and removes duplicate rows from the final result set
  - Performance: May be slower compared to UNION ALL because it involves additional processing to remove duplicates.

```sql

    - SELECT CUSTOMER_ID FROM CUSTOMERS
            UNION
            SELECT CUSTOMER_ID FROM ORDERS
```

![20.1.PNG](img/20.1.PNG)

- UNION ALL (PRINT BOTH AS ITS IS)
  - Purpose: Combines the results of two or more queries without removing duplicates.
  - Performance: Generally faster than UNION because it does not perform the additional step of removing duplicates

```sql
   SELECT CUSTOMER_ID FROM CUSTOMERS
   UNION
   SELECT CUSTOMER_ID FROM ORDERS
```

## UNION ALL

![20.2.PNG](img/20.2.PNG)

## QUE 21 : INNER JOIN - ONLY SHOWS COMMON DATA

```sql
SELECT C.CUSTOMER_ID,C.FIRST_NAME , C.LAST_NAME, C.AGE, O.ORDER_ID , O.ITEM
FROM CUSTOMERS C
INNER JOIN ORDERS O ON C.CUSTOMER_ID=O.CUSTOMER_ID
```

![21.PNG](img/21.PNG)

OR

```sql
SELECT C.CUSTOMER_ID,C.FIRST_NAME , C.LAST_NAME, C.AGE, O.ORDER_ID , O.ITEM
FROM ORDERS O, CUSTOMERS C
WHERE O.CUSTOMER_ID=C.CUSTOMER_ID
```

![21.1.PNG](img/21.1.PNG)

## Q 22: How can we retrieve the names of customers who share the same last name but are from different countries?

```sql
SELECT C1.FIRST_NAME,C1.LAST_NAME ,C1.COUNTRY FROM CUSTOMERS C1
JOIN CUSTOMERS C2
ON C1.LAST_NAME=C2.LAST_NAME WHERE C1.COUNTRY<>C2.COUNTRY
```

![22.PNG](img/22.PNG)

## Q 23: How can we find all customers who share the same first name and are of the same age group (within a 7-year range)?

```sql
SELECT * FROM CUSTOMERS C
JOIN CUSTOMERS C1 ON
C.FIRST_NAME=C1.FIRST_NAME
WHERE c.customer_id < c1.customer_id
    AND ABS(c.age - c1.age) < 5;
```

![23.PNG](img/23.PNG)

## Q 24: HOW TO FIND LAST ROW

```sql
SELECT * FROM `table_name` WHERE id=(SELECT MAX(id) FROM `table_name`);
```

![24.PNG](img/24.PNG)

## QUE 25 : HOW TO FETCH DATA USING LEFT JOIN

![25.PNG](img/25.PNG)
