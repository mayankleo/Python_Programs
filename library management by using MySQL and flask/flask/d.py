import mysql.connector

password = "mayank"
database = "testdb"
table1 = "books"
table2 = "sandi"

def idata():
  mydb = mysql.connector.connect(host="localhost", user="root", password=password, database=database)
  mycursor = mydb.cursor()
  mycursor.execute("""INSERT INTO """+table1+""" (title, author, category) VALUES 
                  ('roots and wings', 'chetna', 'story'),
                  ('grammer plus', 'jainco', 'english'),
                  ('magic', 'ratna sagar', 'story'),
                  ('bliss', 'srijan', 'english'),
                  ('joy of art', 'dev jyoti', 'art'),
                  ('living planet', 'dev sai', 'science'),
                  ('sulekh vikas', 'alphonsa', 'sst'),
                  ('junior science', 'bharti bhavan', 'science'),
                  ('bal ramkatha', 'ganesh rao', 'sst'),
                  ('conversation skills', 'sumit kumar', 'english');""")
  mydb.commit()
  mycursor.execute("""INSERT INTO """+table2+""" (name, uid, book_id, issue, submit) VALUES 
                  ('penny', 10011, 1, '2022-02-16', '2022-02-20'),
                  ('madge', 10012, 2, '2022-03-15', NULL),
                  ('maple', 10013, 3, '2022-04-07', NULL),
                  ('plum', 10014, 4, '2022-05-12', NULL),
                  ('sage', 10015, 5, '2022-06-25', '2022-06-29'),
                  ('verde', 10016, 6, '2022-07-11', '2022-07-21'),
                  ('rowan', 10017, 7, '2022-07-22', NULL), 
                  ('towne', 10018, 8, '2022-08-02', NULL);""")
  mydb.commit()
  mydb.close()

def cifnot():
  global database, password, table1, table2
  mydb = mysql.connector.connect(host="localhost", user="root", password=password)
  mycursor = mydb.cursor()
  mycursor.execute("SHOW DATABASES")
  for databases in mycursor:
    if(databases[0]==database):
      mydb.close()
      return
  mycursor.execute("CREATE DATABASE IF NOT EXISTS "+database)
  mydb.close()
  mydb = mysql.connector.connect(host="localhost", user="root", password=password, database=database)
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE IF NOT EXISTS "+table1+" (id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, title VARCHAR(20) NOT NULL, author VARCHAR(20) NOT NULL, category VARCHAR(20) NOT NULL, quantity SMALLINT UNSIGNED NOT NULL DEFAULT 40)")
  mycursor.execute("CREATE TABLE IF NOT EXISTS "+table2+" (id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) NOT NULL, uid INT UNSIGNED NOT NULL, book_id SMALLINT NOT NULL,  issue DATE NOT NULL, submit DATE)")
  mydb.close()
  idata()