import mysql.connector
from datetime import date
import d

d.cifnot()
con = mysql.connector.connect(host="localhost", user="root", password=d.password, database=d.database)

def addbook():
  bt = input("Book Title:")
  ba = input("Book Author:")
  bc = input("Book Category:")
  bq = input("Book Quantity(default 40):") or "Default"
  comm = con.cursor()
  comm.execute("SELECT title,author,category FROM "+d.table1+" WHERE title =%s AND author =%s AND category =%s",(bt,ba,bc))
  if(comm.fetchall()!=[]):
    return
  con.cursor().execute("INSERT INTO "+d.table1+" (title, author, category, quantity) VALUES(%s,%s,%s,"+bq+")",(bt,ba,bc))
  con.commit()
  main()

def issuebook():
  pn = input("Person Name:")
  pi = input("Person ID(max 5 digits):")
  bid = input("Book ID:")
  idate = input("Date Of Issue(default today):") or date.today().strftime("%Y-%m-%d")
  con.cursor().execute("INSERT INTO "+d.table2+" (name, uid, book_id, issue) VALUES(%s,%s,%s,%s)",(pn,pi,bid,idate))
  con.commit()
  con.cursor().execute("UPDATE "+d.table1+" SET quantity = quantity - 1 WHERE id = "+bid)
  con.commit()
  main()

def submitbook():
  pi = input("Person ID(max 5 digits):")
  bid = input("Book ID:")
  sdate = input("Date Of Submission(default today):") or date.today().strftime("%Y-%m-%d")
  con.cursor().execute("UPDATE "+d.table2+" SET submit = %s  WHERE uid = %s AND book_id = %s",(sdate,pi,bid))
  con.commit()
  con.cursor().execute("UPDATE "+d.table1+" SET quantity = quantity + 1 WHERE id = "+bid)
  con.commit()
  main()

def deletebook():
  bi = input("Book ID:")
  con.cursor().execute("DELETE FROM "+d.table1+" WHERE id = "+bi)
  con.commit()
  main()

def displaybook():
  comm = con.cursor()
  comm.execute("SELECT title,author,category FROM "+d.table1)
  for i in comm.fetchall():
    print("Book Title: ",i[0])
    print("Book Author: ",i[1])
    print("Category: ",i[2])
    print()
  main()

def main():
  print("""----:: LIBRARY MANAGER ::----
  1.DISPLAY BOOKS
  2.ISSUE BOOK
  3.SUBMIT BOOK
  4.ADD BOOK
  5.DELETE BOOK""")
  choice = input("Choice Option:")
  if(choice == '1'):
    displaybook()
  elif(choice =='2'):
    issuebook()
  elif(choice =='3'):
    submitbook()
  elif(choice =='4'):
    addbook()
  elif(choice =='5'):
    deletebook()
  else:
    print("OPTION NOT FOUNT !!")
    main()
main()