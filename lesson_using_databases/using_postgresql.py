#!/usr/bin/python3

# 1. Install PostgreSQL and required things
# sudo apt install postgresql postgresql-contrib libpq-dev
# 2. Start postgresql server
# sudo service postgresql start
# 3. Connect to Postgresql server
# sudo -u postgres psql
# psql
# 4. When connected to PostgreSQL create a new database
# CREATE DATABASE djangodb WITH ENCODING 'utf8' TEMPLATE=template0;
# 5. Create user with password
# CREATE USER django SUPERUSER PASSWORD 'helppoMUISTAA13';
# and then press control-d to exit
# 6. Install posgresql psycopg2 driver to Python 3
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

c.execute("drop table persons") # clean up
conn.commit()
c.close()
conn.close()
