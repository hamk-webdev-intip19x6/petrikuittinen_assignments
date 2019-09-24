#!/usr/bin/python3

# 1. First you must start postgresql service
# sudo service postgresql start
# 2. Second you must connect to Postgresql service, no password
# sudo -u postgres psql
# 3. When connected to PostgreSQL create a new database
# and then press control-d to exit
# create database testdb;
# 4. Install posgresql psycopg2 driver to Python 3
# sudo pip3 install psycopg2

import psycopg2
conn = psycopg2.connect(host="localhost", dbname="djangodb", user="django",
                        password="helppoMUISTAA13")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS persons" +
          "(id integer primary key, name varchar)")
c.execute("insert into persons values(1, 'Jack')")
c.execute("insert into persons values(2, 'Jill')")
c.execute("insert into persons values(3, 'Bob')")
conn.commit()
c.execute("select * from persons")
for id, name in c.fetchall():
    print(id, name)
# clean up
c.execute("drop table persons")
conn.commit()
c.close()
conn.close()
