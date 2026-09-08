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





# cli_input = sys.argv[1]
#
# if cli_input == ".rf":
#     remove_finances(sys.argv[2])
# elif cli_input == ".af":
#     insert_finances(sys.argv[2], sys.argv[3], sys.argv[4])
# elif cli_input == ".uf":
#     update_finances(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
# else:
#     print("Invalid command")


ap.add_argument("-f", "--function", required = True, help = "Function Name")
ap.add_argument("-n", "--name", required=True)
ap.add_argument("-a", "--amount", required=False)
ap.add_argument("-c", "--category", required=False)
ap.add_argument("-i", "--id", required=False)
args = vars(ap.parse_args())

args = vars(ap.parse_args())
print(args)

if args["function"] == "a" :
    insert_finances(args["name"], args["amount"], args["category"])

elif args["function"] == "r" :
    remove_finances(args["name"])

elif args["function"] == "u" :
    update_finances(args["name"], args["amount"], args["category"], args["id"])









conn.close()


















