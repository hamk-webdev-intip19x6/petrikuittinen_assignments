#!/usr/bin/python3
# SQLite comes inbuilt with Python
# Good enough for testing and small usage
import sqlite3
conn = sqlite3.connect("mydatabase.conn") # ":memory" for memory only
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS persons (id int, name text) ")
c.execute("insert into persons values(1, 'Jack')")
c.execute("insert into persons values(2, 'Jill')")
c.execute("insert into persons values(3, 'Bob')")
conn.commit()
for id, name in c.execute("select * from persons"):
    print(id, name)

c.execute("drop table persons")  # clean up
conn.commit()
conn.close()
