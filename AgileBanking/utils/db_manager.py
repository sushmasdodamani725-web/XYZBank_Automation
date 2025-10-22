import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name="agile_banking.db"):
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            balance REAL DEFAULT 0.0
        )""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            type TEXT,
            amount REAL,
            date TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )""")
        self.connection.commit()

    # User methods
    def add_user(self, username, password, role):
        try:
            self.cursor.execute("INSERT INTO users(username,password,role) VALUES (?,?,?)",
                                (username,password,role))
            self.connection.commit()
        except sqlite3.IntegrityError:
            pass

    def validate_login(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
        row = self.cursor.fetchone()
        if row:
            return {"id":row["id"],"username":row["username"],"role":row["role"]}
        return None

    # Customer methods
    def add_customer(self, name, email, balance=0.0):
        try:
            self.cursor.execute("INSERT INTO customers(name,email,balance) VALUES (?,?,?)",
                                (name,email,balance))
            self.connection.commit()
        except sqlite3.IntegrityError:
            pass

    def get_customer_by_email(self,email):
        self.cursor.execute("SELECT * FROM customers WHERE email=?",(email,))
        row = self.cursor.fetchone()
        if row:
            return {"id":row["id"],"name":row["name"],"email":row["email"],"balance":row["balance"]}
        return None

    # Transaction methods
    def add_transaction(self, customer_id, tx_type, amount):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO transactions(customer_id,type,amount,date) VALUES (?,?,?,?)",
                            (customer_id, tx_type, amount, date))
        self.connection.commit()

    def get_transactions(self, customer_id):
        self.cursor.execute("SELECT * FROM transactions WHERE customer_id=?",(customer_id,))
        rows = self.cursor.fetchall()
        return [{"id":r["id"],"type":r["type"],"amount":r["amount"],"date":r["date"]} for r in rows]

    def update_balance(self,email,new_balance):
        self.cursor.execute("UPDATE customers SET balance=? WHERE email=?",(new_balance,email))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
