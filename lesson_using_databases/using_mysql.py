#!/usr/bin/python3

# 1. Install required stuff
# sudo apt -y install mysql-server libmysqlclient-dev
# 2. Configure MySQL
# sudo mysql_secure_installation utility
# 3. Start mysql server (you can stop it with stop command)
# sudo service mysql start
# 4. Connect to mysql server
# sudo mysql -u root -p
# 5. When connected to MySQL create a new database
# create database testdb;
# 6. Add a new user to MySQL 
# INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject) VALUES('petrikuittinen','localhost',PASSWORD('helppo,,MUISTAA13'), '', '', '');
# FLUSH PRIVILEGES;
# GRANT ALL PRIVILEGES ON testdb.* to petrikuittinen@localhost;
# FLUSH PRIVILEGES;
# SHOW GRANTS FOR 'petrikuittinen'@'localhost';
# and then press control-d to exit
# 7. Install mysql driver to Python 3
# sudo pip3 install mysqlclient

import MySQLdb
conn = MySQLdb.connect(host="localhost", user="petrikuittinen",
                     passwd="helppo,,MUISTAA13", db="testdb")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS persons (id int, name varchar(200))")
c.execute("insert into persons values(1, 'Jack')")
c.execute("insert into persons values(2, 'Jill')")
c.execute("insert into persons values(3, 'Bob')")
conn.commit()
c.execute("select * from persons")
for id, name in c.fetchall():
    print(id, name)

c.execute("drop table persons")  # clean up
conn.commit()
c.close()
conn.close()

