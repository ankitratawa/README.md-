# managing database (sqlite3) using python

import sqlite3 as lite
import sys
 
con = lite.connect('system.db')
 
with con:
 
    cur = con.cursor()    
    cur.execute("CREATE TABLE StudntInfo(Id INT, Name TEXT, Age INT)")
    cur.execute("INSERT INTO StudntInfo VALUES(1,'Ankit', 22)")
    cur.execute("INSERT INTO StudntInfo VALUES(2,'Joe',24)")
    cur.execute("INSERT INTO StudntInfo VALUES(3,'Viquash',26)")
 
    cur.execute("CREATE TABLE Job_info(Id INT, Uid INT, Profession TEXT)")
    cur.execute("INSERT INTO Job_info VALUES(1,1,'BI')")
    cur.execute("INSERT INTO Job_info VALUES(2,2,'Marketeer')")
    cur.execute("INSERT INTO Job_info VALUES(3,3,'Salesman')")

# taking out output from database
import sqlite3 as lite
import sys
 
 
con = lite.connect('system.db')
 
with con:    
 
    cur = con.cursor()    #connect two tables and taking name from 1 table along with his profession from second table using inner join function
    cur.execute("SELECT StudntInfo.name, Job_info.profession FROM Job_info INNER JOIN StudntInfo ON StudntInfo.ID = Job_info.uid")
 
    rows = cur.fetchall()
 
    for row in rows:
        print row
