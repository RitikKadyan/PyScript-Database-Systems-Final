import sqlite3
import pandas as pd
from js import console
#python -m http.server 80 | Command to host local server | localhost/file name


def showGames(*ags, **kags):
    db = sqlite3.connect("data.db")
    c = db.cursor()

    sql_query = pd.read_sql_query('''SELECT * FROM games''', db)
    df = pd.DataFrame(sql_query, columns=['g_id', 'g_name', "g_qty_sold"])
    df.rename(columns={'g_id': 'ID', 'g_name': 'Name', 'g_qty_sold': 'Qty Sold'}, inplace=True)
    print(df.to_html(index=False))
    console.log(df)
    c.close()
    db.close()
    
def test_show_games():
    db = sqlite3.connect("data.db")

    sql_query = pd.read_sql_query('''SELECT * FROM games''', db)
    df = pd.DataFrame(sql_query, columns=['g_id', 'g_name', "g_qty_sold"])
    df.rename(columns={'g_id': 'ID', 'g_name': 'Name', 'g_qty_sold': 'Qty Sold'}, inplace=True)
    print(df)

    db.close()

def insertIntoGames(*args, **kwargs):
    db = sqlite3.connect("data.db")
    c = db.cursor()

    game_input = str(Element('game-input').element.value)
    game_qty_input = int(Element('game-qty-input').element.value)
    #if not game_input.element.value or not game_qty_input.element.value: #game_input needs to be input box's id
        #return None
    
    #sql = '''INSERT INTO games VALUES (null, ?, ?)'''
    #db.execute(sql, (game_input.element.value, game_qty_input.element.value))
    #c.execute('''INSERT INTO games VALUES (null, ?, ?), (game_input.value, game_qty_input.value)''')
    c.execute("INSERT INTO games (g_name, g_qty_sold) VALUES ('{}', {})".format(game_input, game_qty_input))
    print(f"executed {game_input}, {game_qty_input}")
    db.commit()
    #print("commited")
    #print(game_input.element.value)

    c.close()
    db.close()

    
def test_insert():
    db = sqlite3.connect("data.db")
    c = db.cursor()

    game = "\"Black Ops\""
    qty = 2
    c.execute(f"INSERT INTO games (g_name, g_qty_sold) VALUES ({game}, {qty})")
    db.commit()

    c.close()
    db.close()


def deleteFromGames(*ags, **kags):
    db = sqlite3.connect("data.db")
    c = db.cursor()

    c.execute("DELETE FROM games WHERE g_id = ?", (4,))
    db.commit()

    c.close()
    db.close()

