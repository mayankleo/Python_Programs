from flask import Flask, render_template, jsonify
import mysql.connector
from datetime import date
import d

d.cifnot()

con = mysql.connector.connect(host="localhost", user="root", password=d.password, database=d.database)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/books')
def books():
    data=[]
    comm = con.cursor()
    comm.execute("SELECT id,title,author,category,quantity FROM "+d.table1)
    for i in comm.fetchall():
        data.append({"id":i[0],"title":i[1],"author":i[2],"category":i[3],"quantity":i[4]})
    return data

@app.route('/delete/<id>')
def delete(id):
    con.cursor().execute("DELETE FROM "+d.table1+" WHERE id = "+id)
    con.commit()
    return jsonify({"status":200})

@app.route('/add/<title>/<author>/<category>')
@app.route('/add/<title>/<author>/<category>/<quantity>')
def add(title,author,category,quantity=''):
  bt, ba, bc = title, author, category
  bq = quantity or "Default"
  comm = con.cursor()
  comm.execute("SELECT title,author,category FROM "+d.table1+" WHERE title =%s AND author =%s AND category =%s",(bt,ba,bc))
  if(comm.fetchall()!=[]):
    return jsonify({"status":200})
  con.cursor().execute("INSERT INTO "+d.table1+" (title, author, category, quantity) VALUES(%s,%s,%s,"+bq+")",(bt,ba,bc))
  con.commit()
  return jsonify({"status":200})


@app.route('/issue/<name>/<uid>/<bookid>')
def issue(name, uid, bookid):
  pn,pi,bid = name,uid,bookid
  idate = date.today().strftime("%Y-%m-%d")
  con.cursor().execute("INSERT INTO "+d.table2+" (name, uid, book_id, issue) VALUES(%s,%s,%s,%s)",(pn,pi,bid,idate))
  con.commit()
  con.cursor().execute("UPDATE "+d.table1+" SET quantity = quantity - 1 WHERE id = "+bid)
  con.commit()
  return jsonify({"status":200})

@app.route('/submit/<uid>/<bookid>')
def submit(uid, bookid):
  pi, bid = uid, bookid
  sdate = date.today().strftime("%Y-%m-%d")
  con.cursor().execute("UPDATE "+d.table2+" SET submit = %s  WHERE uid = %s AND book_id = %s",(sdate,pi,bid))
  con.commit()
  con.cursor().execute("UPDATE "+d.table1+" SET quantity = quantity + 1 WHERE id = "+bid)
  con.commit()
  return jsonify({"status":200})


if __name__ == '__main__':
    app.run()