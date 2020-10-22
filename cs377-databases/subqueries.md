# Subqueries

### Students whose GPA is higher than the average of all GPAS
```
SELECT * 
FROM Student st
WHERE cpga > (SELECT avg(cpga) FROM Student st2);
```

* Queries are evaluated from the inside out

```
SELECT instructor
FROM Offering Off1
WHERE NOT EXISTS (
    SELECT *
    FROM Offering 
    WHERE
    oid <> Off1.oid AND 
    instructor = Off1.instructor
);
```

This subquery has to be reevaluated for each tuple since it contains a reference to `Off1`.

### `EXISTS (subquery)`

* Returns true if the subquery is not empty. False otherwise  
* `NOT EXISTS` is its logical negation.

### Renaming

can make scope explicit.

```
SELECT instructor
FROM Offering Off1
WHERE NOT EXISTS (
    SELECT *
    FROM Offering Off2 
    WHERE
    Off2.oid <> Off1.oid AND 
    Off2.instructor = Off1.instructor
);
```

### Q2 in Exercise sheet

|   R   |       |
| :---: | :---: |
|   a   |   b   |
|   1   |   2   |
|   8   |   7   |
|   5   |       |
|       |   6   |

|   M   |       |
| :---: | :---: |
|   b   |   c   |
|   4   |   3   |
|   7   |   8   |
|       |   5   |
|   6   |       |
|   7   |   1   |

```
SELECT a
FROM R
WHERE b IN ( SELECT b FROM M);
```

* Finds all a's in R where their repective b matches a b in M
* Returns 8 and `NULL` (2 tuples)
* `NULL` is returned because of the matching `b = 6`
* Remember: `NULL` compared to `NULL` returns `NULL`


### Q3

```
CREATE VIEW numOfferings AS(
SELECT dept||cnum AS course, count() as count
FROM (SELECT )
GROUP BY dept, cnum, instructor);

SELECT dept||cnum AS course, instructor, count
FROM numOfferings
WHERE count >= ( SELECT max(count) FROM numOfferings);
```


```
CREATE VIEW courseCounts AS (
SELECT dept||cnum AS course, instructor, count(oid)
FROM Offering
GROUP BY dept, cnum, instructor);

SELECT course, instructor, count
FROM courseCounts c1
WHERE count = (
    SELECT max(count) 
    FROM courseCounts c2
    WHERE c1.course = c2.course);
```