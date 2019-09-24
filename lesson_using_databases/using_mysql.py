#!/usr/bin/python3

# 1. First you must start mysql service (you can stop it with stop command)
# sudo service mysql start
# 2. Second you must connect to mysql service using your C9 username, no password
# mysql --host=localhost --user=petrikuittinen
# 3. When connected to MySQL create a new database and then press control-d to exit
# create database testdb;
# 4. Install mysql driver to Python 3
# sudo pip3 install mysqlclient

import MySQLdb
db = MySQLdb.connect(host="localhost", user="petrikuittinen",
                     passwd="helppo,,MUISTAA13", db="testdb")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS persons (id int, name varchar(200))")
c.execute("insert into persons values(1, 'Jack')")
c.execute("insert into persons values(2, 'Jill')")
c.execute("insert into persons values(3, 'Bob')")
db.commit()
c.execute("select * from persons")
for id, name in c.fetchall():
    print(id, name)
# clean up
c.execute("drop table persons")
db.commit()

