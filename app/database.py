import sqlite3

con = sqlite3.connect(r"C:\coding\app\test.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS dashboard (
        date TEXT,
        item_names TEXT,
        type TEXT,
        sku TEXT,
        quantity INTEGER,
        status TEXT,
        one_price FLOAT,    
        price FLOAT
    )
""", )

cur.execute("""
    INSERT INTO dashboard 
    (date, item_names, type, sku, quantity, status,price)
    VALUES ('12/7/2022', 'Simple Wrleam 1', 'Specializator', 'sku00001', 2, 'sold', 330.0)
""", )


# cur.execute("""
#     INSERT INTO dashboard 
#     (date, item_names, type, sku, quantity, status, total_price)
#     VALUES ('12/7/2022', 'iphone2', 'Specializator', 'sku00001', 2, 'sold', 330.0)
# """, )


cur.execute("""
    INSERT INTO dashboard 
    (date, item_names, type, sku, quantity, status,price)
    VALUES ('12/7/2022', 'iphone8', 'Specializator', 'sku00001', 2, 'sold', 330.0)
""", )

con.commit()
con.close()
