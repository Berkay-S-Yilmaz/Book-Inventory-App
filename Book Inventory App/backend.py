#Backend with SQLite
import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        #conn object that represents connection database (defined in frontend.py)
        #cursor object to execute SQL commands
        #Commits data to database
        #Not using .close() keeping it open to reduce repeating conn and cur objects
        #Defining conn and cur as attributes of Database class, to reuse them in other functions


    #Function to insert data in the database
    def insert(self, title, author, year, isbn):
        #Executing Inster command
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                    (title, author, year, isbn))
        self.conn.commit()

    #View Function (Output)
    def view(self):
        self.cur.execute("SELECT * FROM book")
        #No changes will be made to databse in this funct, thus no commit
        #fetchall() reads all records into memory, and then returns that list.
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    #Function to delete book records in database
    #ID is automatically assigned to each entry in sequential order
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    #Function to Update records (make changes etc)
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                    (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    
