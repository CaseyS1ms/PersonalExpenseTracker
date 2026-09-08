import sqlite3

#DATABASE SETUP
#=====================================================================
conn = sqlite3.connect("finances.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS finances")

table_creation_query = """
    CREATE TABLE finances 
    (
        NAME TEXT NOT NULL,
        AMOUNT INTEGER NOT NULL,
        CATEGORY TEXT NOT NULL
    );
                       """
cursor.execute(table_creation_query)
#===================================================================















conn.close()


















