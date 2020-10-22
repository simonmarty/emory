# Review

## Insert multiple tuples

Put commas between each values set

## Attribute level default

```
create domain CGPA as numeric(10,2)
default 0
check (value >= 0 and value <= 4.0);
```

```
CREATE TABLE AwardNerds (
    sID integer,
    numAwards integer default 0,
    studentGPA CGPA default 5.0);
```

The table above will only throw an error on insertion. Default values are not checked at table instantiatioon.

## Creating a schema

`create schema University;`

## Alter

```
alter table Course
    add column numSections integer;
```

* Suppose table R refers to table S
* You can define fixes that propagate from R to S


```
create table Took (
    foreign key (sID) references Student
        on delete cascade
);
```

* `on delete`
* `on update`
* `on delete restrict on update cascade`

* `restrict`: Don't allow deletion/update
* `cascade`: `-r`
* `set null` set corresponding value in the referring tuple to `null`


Can we add a reaction policy to an existing constraint
* Short answer: No
* drop constraint and add it with the reaction policy (can be done in the same statement)

```
ALTER TABLE Took DROP CONSTRAINT took_sid_fkey,
    ADD CONSTRAINT took_sid_fkey
    foreign key (sid) references student(sid)
    on delete restrict on update cascade;
```