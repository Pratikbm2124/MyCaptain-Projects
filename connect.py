# SQL (Structured Query Language)

import sqlite3

def connect(dbname):
    conn = sqlite3.connect("oyo.db")  # creates a file if it doesnt exist or just connects it to the object

    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")  # (name type)
                 # if the table OYO_HOTELS exists in the file(oyo.db) this does not execute or it creates the table in the file

    print("Table created succesfully!")

    conn.close() # we should always close the connection with the database

def insert_into_table(dbname, values):
    conn = sqlite3.connect("oyo.db")
    insert_sql = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES( ?, ?, ?, ?, ?)"
    conn.execute(insert_sql, values)
                  # this inserts the data into the table

    conn.commit() # in order to keep the connection with the database stable
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect("oyo.db")

    cur = conn.cursor()  # to retrieve the data we need to use this cursor object

    cur.execute("SELECT * FROM OYO_HOTELS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)

    conn.close()
