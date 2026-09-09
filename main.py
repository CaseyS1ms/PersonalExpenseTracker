import sqlite3
import argparse

ap = argparse.ArgumentParser()

#DATABASE SETUP
#=====================================================================
conn = sqlite3.connect("finances.db")
cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS finances")

table_creation_query = """
    CREATE TABLE IF NOT EXISTS finances 
    (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AMOUNT INTEGER NOT NULL,
        CATEGORY TEXT NOT NULL,
        DATE TEXT NOT NULL
    );
                       """
cursor.execute(table_creation_query)
#===================================================================

def insert_finances(name, amount, category, date):
    cursor.execute("INSERT INTO finances  (NAME, AMOUNT, CATEGORY, DATE) VALUES (?,?,?,?)", (name, amount, category, date))
    conn.commit()


def remove_finances(id):
    cursor.execute("DELETE FROM finances WHERE ID = ?", (id,))
    conn.commit()

def update_finances(id, name, amount, category, date):
    cursor.execute("UPDATE finances SET NAME = ?, AMOUNT = ?, CATEGORY = ?, DATE = ? WHERE ID = ?", (name, amount, category, date,  id))
    conn.commit()


def list_finances():
    cursor.execute("SELECT * FROM finances")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def reset_finances():
    cursor.execute("DROP TABLE IF EXISTS finances")
    conn.commit()
    cursor.execute(table_creation_query)
    conn.commit()

def summary_finances():
    cursor.execute("SELECT AMOUNT FROM finances")
    rows = cursor.fetchall()
    amount = 0
    for row in rows:
        amount = amount + row[0]
    print(f"Total - £{amount}")





ap.add_argument("-f", "--function", required = True, help = "Function Name")
ap.add_argument("-n", "--name", required=False)
ap.add_argument("-a", "--amount", required=False)
ap.add_argument("-c", "--category", required=False)
ap .add_argument("-d", "--date", required=False)
ap.add_argument("-i", "--id", required=False)
args = vars(ap.parse_args())

# print(args)

if args["function"] == "a" :
    insert_finances(args["name"], int(args["amount"]), args["category"], args["date"])

elif args["function"] == "r" :
    remove_finances(args["id"])

elif args["function"] == "u" :
    update_finances(args["id"], args["name"], int(args["amount"]), args["category"], args["date"])

elif args["function"] == "l" :
    list_finances()

elif args["function"] == "rt" :
    reset_finances()
    print("succesfully reset database")

elif args["function"] == "s" :
    summary_finances()









conn.close()


















