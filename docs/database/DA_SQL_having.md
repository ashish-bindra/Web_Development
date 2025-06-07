# Grouping Result Sets

- Eleminate duplicates from  a reult set
- How to restrict a result sets

## Eliminating Duplicates - DISTINCT clause

```sql
%load_ext sql
%sql sqlite:///bookstore.db
    
select country from author ORDER BY 1
```

<table>
    <thead>
        <tr>
            <th>Country</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Argentina</td>
        </tr>
        <tr>
            <td>Australia</td>
        </tr>
        <tr>
            <td>Brazil</td>
        </tr>
        <tr>
            <td>Canada</td>
        </tr>
        <tr>
            <td>China</td>
        </tr>
        <tr>
            <td>Colombia</td>
        </tr>
        <tr>
            <td>France</td>
        </tr>
        <tr>
            <td>Germany</td>
        </tr>
        <tr>
            <td>India</td>
        </tr>
        <tr>
            <td>Italy</td>
        </tr>
        <tr>
            <td>Japan</td>
        </tr>
        <tr>
            <td>Mexico</td>
        </tr>
        <tr>
            <td>Netherlands</td>
        </tr>
        <tr>
            <td>Portugal</td>
        </tr>
        <tr>
            <td>Russia</td>
        </tr>
        <tr>
            <td>South Africa</td>
        </tr>
        <tr>
            <td>Spain</td>
        </tr>
        <tr>
            <td>UK</td>
        </tr>
        <tr>
            <td>USA</td>
        </tr>
        <tr>
            <td>USA</td>
        </tr>
    </tbody>
</table>

## The order by clause sorts the result set

## the authors come from the same country, so the result set contains duplicates

```sql
%%sql

select count(country) from author ORDER BY 1
```

<table>
    <thead>
        <tr>
            <th>count(country)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>20</td>
        </tr>
    </tbody>
</table>

```sql
%%sql

select Distinct(country) from author ORDER BY 1
```

<table>
    <thead>
        <tr>
            <th>Country</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Argentina</td>
        </tr>
        <tr>
            <td>Australia</td>
        </tr>
        <tr>
            <td>Brazil</td>
        </tr>
        <tr>
            <td>Canada</td>
        </tr>
        <tr>
            <td>China</td>
        </tr>
        <tr>
            <td>Colombia</td>
        </tr>
        <tr>
            <td>France</td>
        </tr>
        <tr>
            <td>Germany</td>
        </tr>
        <tr>
            <td>India</td>
        </tr>
        <tr>
            <td>Italy</td>
        </tr>
        <tr>
            <td>Japan</td>
        </tr>
        <tr>
            <td>Mexico</td>
        </tr>
        <tr>
            <td>Netherlands</td>
        </tr>
        <tr>
            <td>Portugal</td>
        </tr>
        <tr>
            <td>Russia</td>
        </tr>
        <tr>
            <td>South Africa</td>
        </tr>
        <tr>
            <td>Spain</td>
        </tr>
        <tr>
            <td>UK</td>
        </tr>
        <tr>
            <td>USA</td>
        </tr>
    </tbody>
</table>

```sql
%%sql

select count(Distinct(country)) from author ORDER BY 1
```

<table>
    <thead>
        <tr>
            <th>count(Distinct(country))</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>19</td>
        </tr>
    </tbody>
</table>

## To eliminate duplicates, we use the keyword distinct

```sql
%%sql

select country, count(country) as count from author
Group BY country
```

<table>
    <thead>
        <tr>
            <th>Country</th>
            <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Argentina</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Australia</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Brazil</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Canada</td>
            <td>1</td>
        </tr>
        <tr>
            <td>China</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Colombia</td>
            <td>1</td>
        </tr>
        <tr>
            <td>France</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>1</td>
        </tr>
        <tr>
            <td>India</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Italy</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Japan</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Mexico</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Netherlands</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Portugal</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Russia</td>
            <td>1</td>
        </tr>
        <tr>
            <td>South Africa</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Spain</td>
            <td>1</td>
        </tr>
        <tr>
            <td>UK</td>
            <td>1</td>
        </tr>
        <tr>
            <td>USA</td>
            <td>2</td>
        </tr>
    </tbody>
</table>

## The "group by" clause groups a result into subsets that has matching values for one or more columns

```sql
%%sql

select country, count(country) as count from author
Group BY country
Having count(country) > 3;
```

<table>
    <thead>
        <tr>
            <th>Country</th>
            <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>USA</td>
            <td>4</td>
        </tr>
    </tbody>
</table>

## The "having" clause is used in combination with the "group by" clause

## the "having" clause works only with the "group by" clause
