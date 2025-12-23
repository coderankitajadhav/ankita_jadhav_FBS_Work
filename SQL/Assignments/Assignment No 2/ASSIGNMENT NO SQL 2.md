**ASSIGNMENT NO 2**



**1) Create the table Member, Books and Issue without any constraints as**

**mentioned in the schema description above.**





**FOR MEMBER**



mysql> create table Member

&nbsp;   -> (Member\_id int, Member\_name varchar(30), Member\_address varchar(50

&nbsp;   -> ), Acc\_Open\_Date date, Membership\_type varchar(20), Fees\_paid int, Max\_Book\_Allowed int, Penalty\_Amount decimal(7,2));

Query OK, 0 rows affected (0.14 sec)



**FOR BOOKS**



mysql> create table Books

&nbsp;   -> (Book\_No int,Book\_Name varchar(20),Author\_name varchar(20),

&nbsp;   -> cost decimal(7,2),Category char(10));

Query OK, 0 rows affected (0.03 sec)



**FOR ISSUE**



mysql> create table Issue

&nbsp;   -> (Lib\_Issue\_Id int,Book\_No int,Member\_Id int,Issue\_Date date,Return\_date int);

Query OK, 0 rows affected (0.02 sec)





**2) View the structure of the tables.**



mysql> desc Member;

+-------------------+--------------+------+-----+---------+-------+

| Field             | Type         | Null | Key | Default | Extra |

+-------------------+--------------+------+-----+---------+-------+

| Member\_Id         | int          | YES  |     | NULL    |       |

| Member\_name       | varchar(20)  | YES  |     | NULL    |       |

| Member\_address    | varchar(20)  | YES  |     | NULL    |       |

| Acc\_Open\_Date     | date         | YES  |     | NULL    |       |

| Membership\_type   | varchar(20)  | YES  |     | NULL    |       |

| Fees\_paid         | int          | YES  |     | NULL    |       |

| Max\_Books\_Allowed | int          | YES  |     | NULL    |       |

| Penalty\_Amount    | decimal(7,2) | YES  |     | NULL    |       |

+-------------------+--------------+------+-----+---------+-------+

8 rows in set (0.01 sec)



mysql> desc Books;

+-------------+--------------+------+-----+---------+-------+

| Field       | Type         | Null | Key | Default | Extra |

+-------------+--------------+------+-----+---------+-------+

| Book\_No     | int          | YES  |     | NULL    |       |

| Book\_Name   | varchar(20)  | YES  |     | NULL    |       |

| Author\_name | varchar(20)  | YES  |     | NULL    |       |

| cost        | decimal(7,2) | YES  |     | NULL    |       |

| Category    | char(10)     | YES  |     | NULL    |       |

+-------------+--------------+------+-----+---------+-------+

5 rows in set (0.00 sec)



mysql> desc Issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_Id | int  | YES  |     | NULL    |       |

| Book\_No      | int  | YES  |     | NULL    |       |

| Member\_Id    | int  | YES  |     | NULL    |       |

| Issue\_Date   | date | YES  |     | NULL    |       |

| Return\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



**3) Drop the Member table**



mysql> drop table Member;

Query OK, 0 rows affected (0.02 sec)



mysql> desc Member;

ERROR 1146 (42S02): Table 'fbs.member' doesn't exist



**4) Create the table Member again as per the schema description with the**

**following constraints.**



a. Member\_Id – Primary Key

mysql> create table Member

&nbsp;   -> (Member\_Id int primary key,Member\_name varchar(20),Member\_address varchar(20),Acc\_Open\_Date date,Membership\_type varchar(20),Fees\_paid int,Max\_Books\_Allowed int,Penalty\_Amount decimal(7,2));

Query OK, 0 rows affected (0.03 sec)



mysql> desc Member;

+-------------------+--------------+------+-----+---------+-------+

| Field             | Type         | Null | Key | Default | Extra |

+-------------------+--------------+------+-----+---------+-------+

| Member\_Id         | int          | NO   | PRI | NULL    |       |

| Member\_name       | varchar(20)  | YES  |     | NULL    |       |

| Member\_address    | varchar(20)  | YES  |     | NULL    |       |

| Acc\_Open\_Date     | date         | YES  |     | NULL    |       |

| Membership\_type   | varchar(20)  | YES  |     | NULL    |       |

| Fees\_paid         | int          | YES  |     | NULL    |       |

| Max\_Books\_Allowed | int          | YES  |     | NULL    |       |

| Penalty\_Amount    | decimal(7,2) | YES  |     | NULL    |       |

+-------------------+--------------+------+-----+---------+-------+

8 rows in set (0.00 sec)



b. Membership\_type - ‘Lifetime’,’ Annual’, ‘Half Yearly’,’ Quarterly’



mysql> alter table Member

&nbsp;   -> modify column Membership\_type varchar(20)

&nbsp;   -> check (Membership\_type in("Lifetime","Annual","Half Yearly","Quarterly"));

Query OK, 0 rows affected (0.07 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> show create table Member;

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Table  | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Member | CREATE TABLE `member` (

&nbsp; `Member\_Id` int NOT NULL,

&nbsp; `Member\_name` varchar(20) DEFAULT NULL,

&nbsp; `Member\_address` varchar(20) DEFAULT NULL,

&nbsp; `Acc\_Open\_Date` date DEFAULT NULL,

&nbsp; `Membership\_type` varchar(20) DEFAULT NULL,

&nbsp; `Fees\_paid` int DEFAULT NULL,

&nbsp; `Max\_Books\_Allowed` int DEFAULT NULL,

&nbsp; `Penalty\_Amount` decimal(7,2) DEFAULT NULL,

&nbsp; PRIMARY KEY (`Member\_Id`),

&nbsp; CONSTRAINT `member\_chk\_1` CHECK ((`Membership\_type` in (\_utf8mb4'Lifetime',\_utf8mb4'Annual',\_utf8mb4'Half Yearly',\_utf8mb4'Quarterly')))

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

1 row in set (0.00 sec)



**5)Modify the table Member increase the width of the member name to 30 characters.**



mysql> alter table Member

&nbsp;   -> modify column Member\_name varchar(30);

Query OK, 0 rows affected (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 0



**6) Add a column named as Reference of Char(30) to Issue table.**



mysql> alter table Issue

&nbsp;   -> add column Reference char(30);

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Issue;

+--------------+----------+------+-----+---------+-------+

| Field        | Type     | Null | Key | Default | Extra |

+--------------+----------+------+-----+---------+-------+

| Lib\_Issue\_Id | int      | YES  |     | NULL    |       |

| Book\_No      | int      | YES  |     | NULL    |       |

| Member\_Id    | int      | YES  |     | NULL    |       |

| Issue\_Date   | date     | YES  |     | NULL    |       |

| Return\_date  | int      | YES  |     | NULL    |       |

| Reference    | char(30) | YES  |     | NULL    |       |

+--------------+----------+------+-----+---------+-------+

6 rows in set (0.00 sec)



**7)Delete/Drop the column Reference from Issue.**



mysql> alter table Issue

&nbsp;   -> drop column Reference;

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_Id | int  | YES  |     | NULL    |       |

| Book\_No      | int  | YES  |     | NULL    |       |

| Member\_Id    | int  | YES  |     | NULL    |       |

| Issue\_Date   | date | YES  |     | NULL    |       |

| Return\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



**8)Rename the table Issue to Lib\_Issue.**



mysql> rename table Issue to Lib\_Issue;

Query OK, 0 rows affected (0.02 sec)



mysql> desc Lib\_Issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_Id | int  | YES  |     | NULL    |       |

| Book\_No      | int  | YES  |     | NULL    |       |

| Member\_Id    | int  | YES  |     | NULL    |       |

| Issue\_Date   | date | YES  |     | NULL    |       |

| Return\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



**9)Insert following data in table Member**



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed,Penalty\_Amount)values(1,"Richa Sharma","Pune","10-12-05","Lifetime",25000,5,50);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed)values(2,"Garima Sen","Pune","2025-12-19","Annual",1000,3);

Query OK, 1 row affected (0.01 sec)



mysql> table Member;

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_Id | Member\_name  | Member\_address | Acc\_Open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         1 | Richa Sharma | Pune           | 2010-12-05    | Lifetime        |     25000 |                 5 |          50.00 |

|         2 | Garima Sen   | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

2 rows in set (0.00 sec)



**10)Insert at least 5 records with suitable data.**



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed,Penalty\_Amount)values(3,"Pranali Jadhav","Mumbai","2025-12-20","Half Yearly",2000,1,40);

Query OK, 1 row affected (0.00 sec)



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed,Penalty\_Amount)values(4,"Sayali Lad","Latur","2024-11-21","Lifetime",24000,2,60);

Query OK, 1 row affected (0.00 sec)



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed,Penalty\_Amount)values(5,"Ankita Jadhav","Solapur","2024-09-21","Lifetime",24000,2,60);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed,Penalty\_Amount)values(6,"Sumit Jadhav","Vardha","2023-08-12","Half Yearly",10000,2,20);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_Id,Member\_name,Member\_address,Acc\_Open\_Date,Membership\_type,Fees\_paid,Max\_Books\_Allowed,Penalty\_Amount)values(7,"Sahil Jamdade","Kolkata","2025-12-09","Quarterly",15000,1,70);

Query OK, 1 row affected (0.01 sec)



mysql> table Member;

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_Id | Member\_name    | Member\_address | Acc\_Open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         1 | Richa Sharma   | Pune           | 2010-12-05    | Lifetime        |     25000 |                 5 |          50.00 |

|         2 | Garima Sen     | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

|         3 | Pranali Jadhav | Mumbai         | 2025-12-20    | Half Yearly     |      2000 |                 1 |          40.00 |

|         4 | Sayali Lad     | Latur          | 2024-11-21    | Lifetime        |     24000 |                 2 |          60.00 |

|         5 | Ankita Jadhav  | Solapur        | 2024-09-21    | Lifetime        |     24000 |                 2 |          60.00 |

|         6 | Sumit Jadhav   | Vardha         | 2023-08-12    | Half Yearly     |     10000 |                 2 |          20.00 |

|         7 | Sahil Jamdade  | Kolkata        | 2025-12-09    | Quarterly       |     15000 |                 1 |          70.00 |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

7 rows in set (0.00 sec)



**11) Modify the column Member\_name. Decrease the width of the member**

**name to 20 characters. (If it does not allow state the reason for that)**



mysql> alter table Member

&nbsp;   -> modify column Member\_name varchar(20);

Query OK, 7 rows affected (0.07 sec)

Records: 7  Duplicates: 0  Warnings: 0



**12)Try to insert a record with Max\_Books\_Allowed = 110, Observe the**

**error that comes.**

mysql> insert into member values

-> (8, 'aseet tayade', 'beed', curdate(), 'annual', 1200,110,0);

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'insert into member values
(8, 'aseet tayade', 'beed', curdate(), 'annual', 1200, 110,0' at line 2


**13)Generate another table named Member101 using a Create command**

**along with a simple SQL query on member table.**



mysql> create table Member101(select \* from Member);

Query OK, 7 rows affected (0.02 sec)

Records: 7  Duplicates: 0  Warnings: 0



**14)Add the constraints on columns max\_books\_allowed and penalty\_amt**

**as follows**

**a. max\_books\_allowed < 100**

**b. penalty\_amt maximum 1000**

**Also give names to the constraints.**



mysql> alter table Member

&nbsp;   -> modify column Max\_Books\_Allowed int check(Max\_Books\_Allowed < 100);

Query OK, 7 rows affected (0.07 sec)

Records: 7  Duplicates: 0  Warnings: 0



mysql> alter table Member

&nbsp;   -> modify column Penalty\_Amount decimal(7,2) check(Penalty\_Amount <= 1000);

Query OK, 7 rows affected (0.06 sec)

Records: 7  Duplicates: 0  Warnings: 0



mysql> show create table Member;

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Table  | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Member | CREATE TABLE `member` (

&nbsp; `Member\_Id` int NOT NULL,

&nbsp; `Member\_name` varchar(20) DEFAULT NULL,

&nbsp; `Member\_address` varchar(20) DEFAULT NULL,

&nbsp; `Acc\_Open\_Date` date DEFAULT NULL,

&nbsp; `Membership\_type` varchar(20) DEFAULT NULL,

&nbsp; `Fees\_paid` int DEFAULT NULL,

&nbsp; `Max\_Books\_Allowed` int DEFAULT NULL,

&nbsp; `Penalty\_Amount` decimal(7,2) DEFAULT NULL,

&nbsp; PRIMARY KEY (`Member\_Id`),

&nbsp; CONSTRAINT `member\_chk\_1` CHECK ((`Membership\_type` in (\_utf8mb4'Lifetime',\_utf8mb4'Annual',\_utf8mb4'Half Yearly',\_utf8mb4'Quarterly'))),

&nbsp; CONSTRAINT `member\_chk\_2` CHECK ((`Max\_Books\_Allowed` < 100)),

&nbsp; CONSTRAINT `member\_chk\_3` CHECK ((`Penalty\_Amount` <= 1000))

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

1 row in set (0.00 sec)



**15) Drop the table books.**





mysql> drop table Books;

Query OK, 0 rows affected (0.02 sec)



mysql> desc Books;

ERROR 1146 (42S02): Table 'fbs.books' doesn't exist



**16)Create table Books again as per the schema description with the**

**following constraints.**

**a. Book\_No – Primary Key**

**b. Book\_Name – Not Null**

**c. Category – System, Fiction, Database, RDBMS, Others.**



mysql> create table Books

&nbsp;   -> (Book\_No int primary key,Book\_Name varchar(30) not null,Author\_name varchar(30),Cost decimal (7,2),Category char(10));

Query OK, 0 rows affected (0.02 sec)



mysql> desc Books;

+-------------+--------------+------+-----+---------+-------+

| Field       | Type         | Null | Key | Default | Extra |

+-------------+--------------+------+-----+---------+-------+

| Book\_No     | int          | NO   | PRI | NULL    |       |

| Book\_Name   | varchar(30)  | NO   |     | NULL    |       |

| Author\_name | varchar(30)  | YES  |     | NULL    |       |

| Cost        | decimal(7,2) | YES  |     | NULL    |       |

| Category    | char(10)     | YES  |     | NULL    |       |

+-------------+--------------+------+-----+---------+-------+

5 rows in set (0.01 sec)



c. Category – System, Fiction, Database, RDBMS, Others.



mysql> alter table Books

&nbsp;   -> modify column Category char(10)

&nbsp;   -> check (Category in("System","Fiction","Database","RDBMS","Others"));

Query OK, 0 rows affected (0.06 sec)

Records: 0  Duplicates: 0  Warnings: 0



+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Table | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                     |

+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Books | CREATE TABLE `books` (

&nbsp; `Book\_No` int NOT NULL,

&nbsp; `Book\_Name` varchar(30) NOT NULL,

&nbsp; `Author\_name` varchar(30) DEFAULT NULL,

&nbsp; `Cost` decimal(7,2) DEFAULT NULL,

&nbsp; `Category` char(10) DEFAULT NULL,

&nbsp; PRIMARY KEY (`Book\_No`),

&nbsp; CONSTRAINT `books\_chk\_1` CHECK ((`Category` in (\_utf8mb4'System',\_utf8mb4'Fiction',\_utf8mb4'Database',\_utf8mb4'RDBMS',\_utf8mb4'Others')))

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

1 row in set (0.00 sec)



**17)Insert data in Book table as follows:**



mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_name,Cost,Category)values

&nbsp;   -> (101,"Let us C","Denis Ritchie",450,"System"),

&nbsp;   -> (102,"Oracle-Complete Ref","Loni",550,"Database");

Query OK, 2 rows affected (0.01 sec)

Records: 2  Duplicates: 0  Warnings: 0



mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_name,Cost,Category)values

&nbsp;   -> (103,"Mastering SQL","Loni",250,"Database"),

&nbsp;   -> (104,"PL SQL=Ref","Scott Urman",750,"Database");

Query OK, 2 rows affected (0.01 sec)

Records: 2  Duplicates: 0  Warnings: 0



mysql> table Books;

+---------+---------------------+---------------+--------+----------+

| Book\_No | Book\_Name           | Author\_name   | Cost   | Category |

+---------+---------------------+---------------+--------+----------+

|     101 | Let us C            | Denis Ritchie | 450.00 | System   |

|     102 | Oracle-Complete Ref | Loni          | 550.00 | Database |

|     103 | Mastering SQL       | Loni          | 250.00 | Database |

|     104 | PL SQL=Ref          | Scott Urman   | 750.00 | Database |

+---------+---------------------+---------------+--------+----------+

4 rows in set (0.00 sec)



**18)Insert more records in Book table.**



mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_name,Cost,Category)values

&nbsp;   -> (105,"Wings of fire","Dr Abdul kalam",250,"Others");

Query OK, 1 row affected (0.01 sec)



mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_name,Cost,Category)values

&nbsp;   -> (106,"That Night","Nidhi Upadhyay",350,"Fiction");

Query OK, 1 row affected (0.01 sec)



mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_name,Cost,Category)values

&nbsp;   -> (107,"The Database Book","Narain Gehani",150,"Database");

Query OK, 1 row affected (0.01 sec)



**19)View the data in the tables using simple SQL query.**

**mysql> table Books;**

+---------+---------------------+----------------+--------+----------+

| Book\_No | Book\_Name           | Author\_name    | Cost   | Category |

+---------+---------------------+----------------+--------+----------+

|     101 | Let us C            | Denis Ritchie  | 450.00 | System   |

|     102 | Oracle-Complete Ref | Loni           | 550.00 | Database |

|     103 | Mastering SQL       | Loni           | 250.00 | Database |

|     104 | PL SQL=Ref          | Scott Urman    | 750.00 | Database |

|     105 | Wings of fire       | Dr Abdul kalam | 250.00 | Others   |

|     106 | That Night          | Nidhi Upadhyay | 350.00 | Fiction  |

|     107 | The Database Book   | Narain Gehani  | 150.00 | Database |

+---------+---------------------+----------------+--------+----------+

7 rows in set (0.00 sec)



**20)Insert into Book following data.**



mysql> alter table Books

&nbsp;   -> drop constraint books\_chk\_1;

Query OK, 0 rows affected (0.12 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_Name,Cost,Category)values(105,"National geograhic","Adis scott",1000,"science");

Query OK, 1 row affected (0.02 sec)



mysql> table Books;

+---------+---------------------------+---------------------+------+----------+

| Book\_No | Book\_Name                 | Author\_Name         | Cost | Category |

+---------+---------------------------+---------------------+------+----------+

|     101 | Let us c                  | Dennis Ritchie      |  450 | system   |

|     102 | Oracle-Complete Ref       | Loni                |  250 | databse  |

|     103 | Mastering SQL             | Loni                |  250 | databse  |

|     104 | PL SQL-Ref                | Scott Urman         |  750 | databse  |

|     105 | National geograhic        | Adis scott          | 1000 | science  |

|     106 | Wings of fire             | Dr. APJ Abdul kalam |  180 | Others   |

|     107 | Operating system Concepts | WILEY               |  400 | system   |

+---------+---------------------------+---------------------+------+----------+

7 rows in set (0.01 sec)



**21)Rename the table Lib\_Issue to Issue.**



mysql> rename table Lib\_Issue to Issue;

Query OK, 0 rows affected (0.03 sec)



**22) Drop table Issue.**



mysql> drop table Issue;

Query OK, 0 rows affected (0.02 sec)



mysql> desc Issue;

ERROR 1146 (42S02): Table 'fbs.issue' doesn't exist



**23) As per the given structure Create table Issue again with following**

**constraints.**



 Lib\_Issue\_Id-Primary key

 Book\_No- foreign key

 Member\_id - foreign key

 Issue\_date

 Return\_date



mysql> create table Issue

&nbsp;   -> (Lib\_Issue\_Id int,Book\_No int,Member\_Id int,Issue\_Date date,Return\_date int);

Query OK, 0 rows affected (0.03 sec)



mysql> alter table Issue

&nbsp;   -> add primary key(Lib\_Issue\_Id);

Query OK, 0 rows affected (0.07 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Issue

&nbsp;   -> add foreign key (Book\_No)

&nbsp;   -> references Books(Book\_No);

Query OK, 0 rows affected (0.17 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Issue

&nbsp;   -> add foreign key(Member\_Id)

&nbsp;   -> references Member(Member\_Id);

Query OK, 0 rows affected (0.09 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_Id | int  | NO   | PRI | NULL    |       |

| Book\_No      | int  | YES  | MUL | NULL    |       |

| Member\_Id    | int  | YES  | MUL | NULL    |       |

| Issue\_Date   | date | YES  |     | NULL    |       |

| Return\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



**24)Insert following data into Issue table.**



mysql> insert into Issue

&nbsp;   -> (Lib\_Issue\_Id,Book\_No,Member\_Id,Issue\_Date)values

&nbsp;   -> (7002,102,2,"2006-12-25"),

&nbsp;   -> (7003,104,1,"2006-11-15"),

&nbsp;   -> (7004,101,1,"2006-07-04"),

&nbsp;   -> (7005,104,2,"2006-11-15"),

&nbsp;   -> (7006,101,3,"2006-02-18");

Query OK, 5 rows affected (0.01 sec)

Records: 5  Duplicates: 0  Warnings: 0



mysql> table Issue;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_Id | Book\_No | Member\_Id | Issue\_Date | Return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-06 |        NULL |

|         7002 |     102 |         2 | 2006-12-25 |        NULL |

|         7003 |     104 |         1 | 2006-11-15 |        NULL |

|         7004 |     101 |         1 | 2006-07-04 |        NULL |

|         7005 |     104 |         2 | 2006-11-15 |        NULL |

|         7006 |     101 |         3 | 2006-02-18 |        NULL |

+--------------+---------+-----------+------------+-------------+

6 rows in set (0.00 sec)



**25)Remove the constraints on Issue table**


**TO REMOVE PRIMARY KEY CONSTRAINT**

mysql> alter table Issue

&nbsp;   -> drop primary key;

Query OK, 6 rows affected (0.10 sec)

Records: 6  Duplicates: 0  Warnings: 0



mysql> desc Issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_Id | int  | NO   |     | NULL    |       |

| Book\_No      | int  | YES  | MUL | NULL    |       |

| Member\_Id    | int  | YES  | MUL | NULL    |       |

| Issue\_Date   | date | YES  |     | NULL    |       |

| Return\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



**FOR REMOVE CONSTRAINTS FOREIGN KEY** 



mysql> alter table Issue

&nbsp;   -> drop constraint issue\_ibfk\_1;

Query OK, 0 rows affected (0.02 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> show create table Issue;

+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Table | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                     |

+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Issue | CREATE TABLE `issue` (

&nbsp; `Lib\_Issue\_Id` int NOT NULL,

&nbsp; `Book\_No` int DEFAULT NULL,

&nbsp; `Member\_Id` int DEFAULT NULL,

&nbsp; `Issue\_Date` date DEFAULT NULL,

&nbsp; `Return\_date` int DEFAULT NULL,

&nbsp; PRIMARY KEY (`Lib\_Issue\_Id`),

&nbsp; KEY `Book\_No` (`Book\_No`),

&nbsp; KEY `Member\_Id` (`Member\_Id`),

&nbsp; CONSTRAINT `issue\_ibfk\_2` FOREIGN KEY (`Member\_Id`) REFERENCES `member` (`Member\_Id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

1 row in set (0.00 sec)



mysql> alter table Issue

&nbsp;   -> drop constraint issue\_ibfk\_2;

Query OK, 0 rows affected (0.02 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> show create table Issue;

+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Table | Create Table                                                                                                                                                                                                                                                                                                            |

+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Issue | CREATE TABLE `issue` (

&nbsp; `Lib\_Issue\_Id` int NOT NULL,

&nbsp; `Book\_No` int DEFAULT NULL,

&nbsp; `Member\_Id` int DEFAULT NULL,

&nbsp; `Issue\_Date` date DEFAULT NULL,

&nbsp; `Return\_date` int DEFAULT NULL,

&nbsp; KEY `Book\_No` (`Book\_No`),

&nbsp; KEY `Member\_Id` (`Member\_Id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

1 row in set (0.00 sec)



**26) Insert a record in Issue table. The member\_id should not exist in member table.**



mysql> insert into Issue

&nbsp;   -> (Lib\_Issue\_Id,Book\_No,Member\_Id,Issue\_Date)values

&nbsp;   -> (7007,107,4,"2006-12-1");

Query OK, 1 row affected (0.01 sec)



mysql> table Issue;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_Id | Book\_No | Member\_Id | Issue\_Date | Return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-06 |        NULL |

|         7002 |     102 |         2 | 2006-12-25 |        NULL |

|         7003 |     104 |         1 | 2006-11-15 |        NULL |

|         7004 |     101 |         1 | 2006-07-04 |        NULL |

|         7005 |     104 |         2 | 2006-11-15 |        NULL |

|         7006 |     101 |         3 | 2006-02-18 |        NULL |

|         7007 |     107 |         4 | 2006-12-01 |        NULL |

+--------------+---------+-----------+------------+-------------+

7 rows in set (0.00 sec)



**27) Now enable the constraints of Issue table. Observe the error**

mysql> alter table issue

-> add primary key(lib_issue_id);

ERROR 1068 (42000): Multiple primary key defined

mysql> alter table issue

-> add foreign key(book_no)

-> references books (book_no); 

affected (0.07 sec)

Query OK, 7 rows Records: 7 Duplicates: 0 Warnings:

mysql> alter table issue

-> add foreign key(member_id)

-> references member(member_id);

ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (store. @sql-12cc_2c", CONSTRAINT "issue_ibfk 2 FOREIGN KEY (member id') REFERENCES member (`member_id')) I

**28) Delete the record inserted at Q-27) and enable the constraints.**

mysql> delete from issue

-> where member id 999;

Query OK, 1 row affected (0.00 sec)

mysql> alter table issue

-> add primary key(lib_issue_id); 

ERROR 1068 (42000): Multiple primary key defined

mysql> alter table issue

->add foreign key(book_no)

-> references books (book_no);

Query OK, 6 rows affected (0.09 sec) Records: 6 Duplicates: Warnings: 0

mysql>alter table issue

->add foreign key(member_id)

->references member(member_id);

Query OK, 6 rows affected (0.09 sec) Records: 6 Duplicates: 0 Warnings: 0


**29) Try to delete the record of member id 1 from member table and**

**observe the error.**



mysql> delete from Member

&nbsp;   -> where Member\_id=1;

Query OK, 1 row affected (0.01 sec)



mysql> table Member;

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_Id | Member\_name    | Member\_address | Acc\_Open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         2 | Garima Sen     | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

|         3 | Pranali Jadhav | Mumbai         | 2025-12-20    | Half Yearly     |      2000 |                 1 |          40.00 |

|         4 | Sayali Lad     | Latur          | 2024-11-21    | Lifetime        |     24000 |                 2 |          60.00 |

|         5 | Ankita Jadhav  | Solapur        | 2024-09-21    | Lifetime        |     24000 |                 2 |          60.00 |

|         6 | Sumit Jadhav   | Vardha         | 2023-08-12    | Half Yearly     |     10000 |                 2 |          20.00 |

|         7 | Sahil Jamdade  | Kolkata        | 2025-12-09    | Quarterly       |     15000 |                 1 |          70.00 |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

6 rows in set (0.00 sec)





**30) View the data and structure of all the three tables Member,Issue, Book.**



**FOR MEMBER**



mysql> desc Member;

+-------------------+--------------+------+-----+---------+-------+

| Field             | Type         | Null | Key | Default | Extra |

+-------------------+--------------+------+-----+---------+-------+

| Member\_Id         | int          | NO   | PRI | NULL    |       |

| Member\_name       | varchar(20)  | YES  |     | NULL    |       |

| Member\_address    | varchar(20)  | YES  |     | NULL    |       |

| Acc\_Open\_Date     | date         | YES  |     | NULL    |       |

| Membership\_type   | varchar(20)  | YES  |     | NULL    |       |

| Fees\_paid         | int          | YES  |     | NULL    |       |

| Max\_Books\_Allowed | int          | YES  |     | NULL    |       |

| Penalty\_Amount    | decimal(7,2) | YES  |     | NULL    |       |

+-------------------+--------------+------+-----+---------+-------+

8 rows in set (0.00 sec)



mysql> table Member;

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_Id | Member\_name    | Member\_address | Acc\_Open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         2 | Garima Sen     | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

|         3 | Pranali Jadhav | Mumbai         | 2025-12-20    | Half Yearly     |      2000 |                 1 |          40.00 |

|         4 | Sayali Lad     | Latur          | 2024-11-21    | Lifetime        |     24000 |                 2 |          60.00 |

|         5 | Ankita Jadhav  | Solapur        | 2024-09-21    | Lifetime        |     24000 |                 2 |          60.00 |

|         6 | Sumit Jadhav   | Vardha         | 2023-08-12    | Half Yearly     |     10000 |                 2 |          20.00 |

|         7 | Sahil Jamdade  | Kolkata        | 2025-12-09    | Quarterly       |     15000 |                 1 |          70.00 |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

6 rows in set (0.00 sec)



**FOR ISSUE**



mysql> desc Issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_Id | int  | NO   |     | NULL    |       |

| Book\_No      | int  | YES  | MUL | NULL    |       |

| Member\_Id    | int  | YES  | MUL | NULL    |       |

| Issue\_Date   | date | YES  |     | NULL    |       |

| Return\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



mysql> table Issue;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_Id | Book\_No | Member\_Id | Issue\_Date | Return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-06 |        NULL |

|         7002 |     102 |         2 | 2006-12-25 |        NULL |

|         7003 |     104 |         1 | 2006-11-15 |        NULL |

|         7004 |     101 |         1 | 2006-07-04 |        NULL |

|         7005 |     104 |         2 | 2006-11-15 |        NULL |

|         7006 |     101 |         3 | 2006-02-18 |        NULL |

|         7007 |     107 |         4 | 2006-12-01 |        NULL |

+--------------+---------+-----------+------------+-------------+

7 rows in set (0.00 sec)



**FOR BOOKS**



mysql> desc Books;

+-------------+--------------+------+-----+---------+-------+

| Field       | Type         | Null | Key | Default | Extra |

+-------------+--------------+------+-----+---------+-------+

| Book\_No     | int          | NO   | PRI | NULL    |       |

| Book\_Name   | varchar(30)  | NO   |     | NULL    |       |

| Author\_name | varchar(30)  | YES  |     | NULL    |       |

| Cost        | decimal(7,2) | YES  |     | NULL    |       |

| Category    | char(10)     | YES  |     | NULL    |       |

+-------------+--------------+------+-----+---------+-------+

5 rows in set (0.00 sec)



mysql> table Books;

+---------+---------------------------+---------------------+------+----------+

| Book\_No | Book\_Name                 | Author\_Name         | Cost | Category |

+---------+---------------------------+---------------------+------+----------+

|     101 | Let us c                  | Dennis Ritchie      |  450 | system   |

|     102 | Oracle-Complete Ref       | Loni                |  250 | databse  |

|     103 | Mastering SQL             | Loni                |  250 | databse  |

|     104 | PL SQL-Ref                | Scott Urman         |  750 | databse  |

|     105 | National geograhic        | Adis scott          | 1000 | science  |

|     106 | Wings of fire             | Dr. APJ Abdul kalam |  180 | Others   |

|     107 | Operating system Concepts | WILEY               |  400 | system   |

+---------+---------------------------+---------------------+------+----------+



**31) Modify the Return\_Date of 7004,7005 to 15 days after the Issue\_date.**



mysql> update issue set Return\_date=Issue\_Date+15

&nbsp;   -> where Lib\_Issue\_Id in (7004,7005);

Query OK, 2 rows affected (0.01 sec)

Rows matched: 2  Changed: 2  Warnings: 0



mysql> table Issue;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_Id | Book\_No | Member\_Id | Issue\_Date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-06 | NULL        |

|         7002 |     102 |         2 | 2006-12-25 | NULL        |

|         7003 |     104 |         1 | 2006-11-15 | NULL        |

|         7004 |     101 |         1 | 2006-07-04 | 2006-07-19  |

|         7005 |     104 |         2 | 2006-11-15 | 2006-11-30  |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

|         7007 |     107 |         4 | 2006-12-01 | NULL        |

+--------------+---------+-----------+------------+-------------+

7 rows in set (0.00 sec)



**32) Remove all the records from Issue table where member\_ID is 1**

**and Issue date in before 10-Dec-06.**





mysql> delete from Issue

&nbsp;   -> where Member\_Id=1 and Issue\_Date<"2006-12-06";

Query OK, 2 rows affected (0.01 sec)



mysql> table Issue;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_Id | Book\_No | Member\_Id | Issue\_Date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-06 | NULL        |

|         7002 |     102 |         2 | 2006-12-25 | NULL        |

|         7005 |     104 |         2 | 2006-11-15 | 2006-11-30  |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

|         7007 |     107 |         4 | 2006-12-01 | NULL        |

+--------------+---------+-----------+------------+-------------+

5 rows in set (0.00 sec)



**33) Remove all the records from Book table with category other**

**than RDBMS and Database.**

mysql> delete from Books

-> where Category not in("RDBMS","Database");

Query OK, 7 rows affected (0.01 sec)

mysql> table Books;
Empty set (0.00 sec)

**34) Remove the table Member.**

mysql> drop table Member;

Query OK, 0 rows affected (0.02 sec)



mysql> desc Member;

ERROR 1146 (42S02): Table 'fbs.member' doesn't exist





**35) Remove the table Book.**

mysql> drop table Books;

Query OK, 0 rows affected (0.02 sec)



mysql> desc Books;

ERROR 1146 (42S02): Table 'fbs.books' doesn't exist





