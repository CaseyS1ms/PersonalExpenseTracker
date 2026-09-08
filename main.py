import sqlite3


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
        CATEGORY TEXT NOT NULL
    );
                       """
cursor.execute(table_creation_query)
#===================================================================

def insert_finances(name, amount, category):
    cursor.execute("INSERT INTO finances  (NAME, AMOUNT, CATEGORY) VALUES (?,?,?)", (name, amount, category))
    conn.commit()


def remove_finances(name):
    cursor.execute("DELETE FROM finances WHERE NAME = ?", (name,))
    conn.commit()

def update_finances(id, name, amount, category):
    cursor.execute("UPDATE finances SET NAME = ?, AMOUNT = ?, CATEGORY = ? WHERE ID = ?", (name, amount, category, id))
    conn.commit()





insert_finances("John", "5000", "RENT")


update_finances("1","John", "500", "BILLS")









conn.close()


















