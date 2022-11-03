import sqlite3
import pandas as pd

#python -m http.server | Command to host local server 
db = sqlite3.connect("data.db")
c = db.cursor()

def showGames(*ags, **kags):
    sql_query = pd.read_sql_query('''SELECT * FROM games''', db)
    df = pd.DataFrame(sql_query, columns=['g_id', 'g_name', "g_qty_sold"])
    df.rename(columns={'g_id': 'ID', 'g_name': 'Name', 'g_qty_sold': 'Qty Sold'}, inplace=True)
    print(df.to_html(index=False))
    

def insertIntoGames(*ags, **kags):
    #if not game_input.element.value or not game_qty_input.value: #game_input needs to be input box's id
        #return None
    
    c.execute("INSERT INTO games VALUES (null, ?, ?)", ('GTA 5', 10))
    #c.execute("INSERT INTO games (g_name, g_qty_sold) VALUES (\"GTA 4\", 4)")
    db.commit()

def deleteFromGames(*ags, **kags):
    c.execute("DELETE FROM games WHERE g_id = ?", (2,))
    db.commit()

