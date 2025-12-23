**ASSIGNMENT NO 1**





**Q1.Login to MySQL and view all databases already present. You should get following result:**



mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| fbs                |

| information\_schema |

| mysql              |

| performance\_schema |

| student            |

| sys                |

+--------------------+

6 rows in set (0.06 sec)



**Q2.Write an SQL statement to create a simple table countries including columns**

**country\_id,country\_name and region\_id. After this display the structure of table as below:**



mysql> create table Counteries

&nbsp;   -> (Country\_id int,Country\_name varchar(20),region\_id int);

Query OK, 0 rows affected (0.05 sec)



mysql> desc Counteries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| Country\_id   | int         | YES  |     | NULL    |       |

| Country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.01 sec)





**Q3. Write an SQL statement to create a table named jobs including columns**

**job\_id, job\_title, min\_salary, max\_salary and check whether the**

**max\_salary amount exceeding the upper limit 25000. Also set job\_id as**

**primary key and entering null values for job\_title is not allowed.?**



mysql> create table Jobs

&nbsp;   -> (job\_id int,job\_title varchar(20),min\_salary int,max\_salary int);

Query OK, 0 rows affected (0.03 sec)



mysql> desc Jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | YES  |     | NULL    |       |

| job\_title  | varchar(20) | YES  |     | NULL    |       |

| min\_salary | int         | YES  |     | NULL    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql> alter table Jobs

&nbsp;   -> add primary key(job\_id);

Query OK, 0 rows affected (0.06 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Jobs

&nbsp;   -> modify column job\_title varchar(20) not null;

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Jobs

&nbsp;   -> modify column max\_salary int check(max\_salary <= 25000);

Query OK, 0 rows affected (0.07 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(20) | NO   |     | NULL    |       |

| min\_salary | int         | YES  |     | NULL    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql> alter table Jobs

&nbsp;   -> modify column max\_salary int check(max\_salary <= 25000);

Query OK, 0 rows affected (0.07 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> insert into Jobs

&nbsp;   -> (job\_id,job\_title,min\_salary,max\_salary)values

&nbsp;   -> (101,"Assistant",10000,24000);

Query OK, 1 row affected (0.01 sec)



mysql> table Jobs;

+--------+-----------+------------+------------+

| job\_id | job\_title | min\_salary | max\_salary |

+--------+-----------+------------+------------+

|    101 | Assistant |      10000 |      24000 |

+--------+-----------+------------+------------+

1 row in set (0.00 sec)



**Q4 Write a SQL statement to create a table named job\_histry including columns**

**employee\_id, start\_date, end\_date, job\_id and department\_id:**





mysql> create table job\_history

&nbsp;   -> (employee\_id int,start\_date int,end\_date int,job\_id int,department\_idint);

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 2

mysql> create table job\_history

&nbsp;   -> (employee\_id int,start\_date int,end\_date int,job\_id int,department\_id int);

Query OK, 0 rows affected (0.02 sec)



mysql> desc job\_history;

+---------------+------+------+-----+---------+-------+

| Field         | Type | Null | Key | Default | Extra |

+---------------+------+------+-----+---------+-------+

| employee\_id   | int  | YES  |     | NULL    |       |

| start\_date    | int  | YES  |     | NULL    |       |

| end\_date      | int  | YES  |     | NULL    |       |

| job\_id        | int  | YES  |     | NULL    |       |

| department\_id | int  | YES  |     | NULL    |       |

+---------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



**Q5. Write an SQL statement to alter a table named countries to make sure that no**

**duplicate data against column country\_id will be allowed at the time of insertion:**



mysql> alter table Counteries

&nbsp;   -> modify column Country\_id int unique;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Counteries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| Country\_id   | int         | YES  | UNI | NULL    |       |

| Country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



**Q6.Write an SQL statement to create a table named jobs including columns job\_id,**

**job\_title, min\_salary and max\_salary, and make sure that, the default value**

**for job\_title is blank and min\_salary is 8000 and max\_salary is NULL will be**

**entered automatically at the time of insertion if no value assigned for the specified columns:**



mysql> alter table Jobs

&nbsp;   -> modify column job\_title varchar(20) default '',

&nbsp;   -> modify column min\_salary int default 8000,

&nbsp;   -> modify column max\_salary int default NULL;

Query OK, 0 rows affected (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(20) | YES  |     |         |       |

| min\_salary | int         | YES  |     | 8000    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



**Q7.Create a Department table with following structure:**





mysql> create table Department;

mysql> create table Department

&nbsp;   -> (DEPARTMENT\_ID decimal(4,0),DEPARTMENT\_NAME varchar(30),

&nbsp;   -> MANAGER\_ID decimal(6,0),LOCATION\_ID decimal(4,0));

Query OK, 0 rows affected (0.03 sec)



mysql> alter table Department

&nbsp;   -> add primary key(DEPARTMENT\_ID,MANAGER\_ID);

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Department

&nbsp;   -> modify column DEPARTMENT\_ID DECIMAL(4,0) default 0,

&nbsp;   -> modify column MANAGER\_ID DECIMAL(6,0) default 0;

Query OK, 0 rows affected (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Department

&nbsp;   -> modify column DEPARTMENT\_NAME varchar(20) not null;

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Department;

+-----------------+--------------+------+-----+---------+-------+

| Field           | Type         | Null | Key | Default | Extra |

+-----------------+--------------+------+-----+---------+-------+

| DEPARTMENT\_ID   | decimal(4,0) | NO   | PRI | 0       |       |

| DEPARTMENT\_NAME | varchar(30)  | NO   |     | NULL    |       |

| MANAGER\_ID      | decimal(6,0) | NO   | PRI | 0       |       |

| LOCATION\_ID     | decimal(4,0) | YES  |     | NULL    |       |

+-----------------+--------------+------+-----+---------+-------+

4 rows in set (0.00 sec)





**Q8. Write an SQL statement to create a table employees including columns**

**employee\_id, first\_name, last\_name, email, phone\_number hire\_date, job\_id,**

**salary, commission, manager\_id and department\_id and make sure that, the**

**employee\_id column does not contain any duplicate value at the time of**

**insertion and the foreign key columns combined by department\_id and**

**manager\_id columns contain only those unique combination values, which**

**combinations are exists in the departments table:**







mysql> create table Employees

&nbsp;   -> (emp\_id int,first\_name varchar(20),last\_name varchar(20),

&nbsp;   -> email\_id varchar(20),phone\_number int,hire\_date int,job\_id int,

&nbsp;   -> salary int,commission int,manager\_id int,department\_id int);

Query OK, 0 rows affected (0.03 sec)





mysql> alter table Employees

&nbsp;   -> add primary key(emp\_id);

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Employees

&nbsp;   -> modify department\_id decimal(4,0),

&nbsp;   -> modify manager\_id decimal(6,0);

Query OK, 0 rows affected (0.07 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Employees

&nbsp;   -> add constraint fk\_dept\_manager

&nbsp;   -> foreign key (department\_id,manager\_id)

&nbsp;   -> references department(department\_id,manager\_id);

Query OK, 0 rows affected (0.10 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Employees;

+---------------+--------------+------+-----+---------+-------+

| Field         | Type         | Null | Key | Default | Extra |

+---------------+--------------+------+-----+---------+-------+

| emp\_id        | int          | NO   | PRI | NULL    |       |

| first\_name    | varchar(20)  | YES  |     | NULL    |       |

| last\_name     | varchar(20)  | YES  |     | NULL    |       |

| email\_id      | varchar(20)  | YES  |     | NULL    |       |

| phone\_number  | int          | YES  |     | NULL    |       |

| hire\_date     | int          | YES  |     | NULL    |       |

| job\_id        | int          | YES  |     | NULL    |       |

| salary        | int          | YES  |     | NULL    |       |

| commission    | int          | YES  |     | NULL    |       |

| manager\_id    | decimal(6,0) | YES  |     | NULL    |       |

| department\_id | decimal(4,0) | YES  | MUL | NULL    |       |

+---------------+--------------+------+-----+---------+-------+







































