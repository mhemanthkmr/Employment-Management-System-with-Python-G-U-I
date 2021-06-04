import sqlite3

class Database :
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    #Insert Function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.con.commit()

    #Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        return rows

    # Delete a Records in DB
    def remove(self,id):
        self.cur.execute("delete from employees WHERE id=?",(id,))
        self.con.commit()

    # Update a Record in DB
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",(name,age,doj,email,gender,contact,address,id))
        self.con.commit()
o = Database("Employee.db")
# o.insert("Hemanth Kumar","18","03-05-2003","m.hemanthkmr143@gmail.com","Male","8072764866","Hello 77")
