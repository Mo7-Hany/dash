from  flask import Flask,render_template,request
import sqlite3

Dashboard = Flask(__name__)


def get_db_connection():
    con = sqlite3.connect(r"C:\coding\app\test.db")
    con.row_factory = sqlite3.Row 
    cur = con.execute('SELECT rowid, * FROM dashboard')
    data= cur.fetchall()
    return data


def search_db():
    con = sqlite3.connect(r"C:\coding\app\test.db")
    con.row_factory = sqlite3.Row 
    cur = con.execute('SELECT * FROM  dashboard WHERE item_names LIKE "i%"')
    data= cur.fetchall()
    return data


def search_inventory_db(search_word):
    con = sqlite3.connect(r"C:\coding\app\test.db")
    con.row_factory = sqlite3.Row 
    cur = con.execute('SELECT * FROM  dashboard WHERE item_names LIKE "%{search_word}%"'.format(search_word=search_word))
    data= cur.fetchall()
    return data

def add_db(date,kind,item_name,status,sku,quantity,price):
    con = sqlite3.connect(r"C:\coding\app\test.db")
    con.row_factory = sqlite3.Row 
    con.execute('INSERT INTO dashboard (date,item_names, type, status, sku, quantity,  price) VALUES ("{date}","{item_name}", "{kind}","{status}", "{sku}", {quantity},  {price})'.format(date=date,item_name=item_name,kind=kind,status=status,sku=sku,quantity=quantity,price=price))
    con.commit()
    con.close()
    return None


def search_pos_db(search_word):
    con = sqlite3.connect(r"C:\coding\app\test.db")
    con.row_factory = sqlite3.Row 
    cur = con.execute('SELECT * FROM  dashboard WHERE sku LIKE "{search_word}"'.format(search_word=search_word))
    data= cur.fetchall()
    return data



@Dashboard.route("/") 
def homepage () :
    return render_template('index.html',data=get_db_connection())




@Dashboard.route("/search" ,methods=["get"]) 
def inventory () :
    search_word=request.args.get('s')
    return render_template('inventory.html',data=search_inventory_db(search_word))
    



@Dashboard.route("/add",methods=["GET", "POST"]) 
def add() :
    if request.method == "POST":  
      print("form submitted")
      kind=request.form.get('type')
      item=request.form.get('item_name')      
      status=request.form.get('status')     
      sku=request.form.get('sku')      
      quntity=request.form.get('quantity')      
      date=request.form.get('date')     
      price=request.form.get('price')
      add_db(date,kind,item,status,sku,quntity,price)
    return render_template('add.html')



@Dashboard.route("/pos",methods=["GET", "POST"])
def pos():
    search_word=request.args.get('s')
    return render_template('pos.html',data=search_pos_db(search_word))



if __name__ == '__main__' :
    Dashboard.run(debug=True,port=1000)

