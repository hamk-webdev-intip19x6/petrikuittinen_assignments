#!/usr/bin/python3

import sqlite3
db = sqlite3.connect("mydatabase.db") # ":memory" for memory only
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS persons (id int, name text) ")
c.execute("insert into persons values(1, 'Jack')")
c.execute("insert into persons values(2, 'Jill')")
c.execute("insert into persons values(3, 'Bob')")
db.commit()
for id, name in c.execute("select * from persons"):
    print(id, name)
# clean up
c.execute("drop table persons")
db.commit()
    
