import sqlite3

def create_connection():
    conn = sqlite3.connect('Auth.db',check_same_thread=False)
    print("database connect successfully")
    return conn

connection = create_connection()
cursor  = connection.cursor()

def register(data):
    try:
        cursor.execute("""INSERT INTO Authen (username,email,password) VALUES (?,?,?)""",data)
        connection.commit()
        return True
    except Exception as e : 
        print("error is", e)
        return False

def check_login(data):
    try:
        # cursor = connetion.cursor()
        cursor.execute("SELECT * FROM Authen WHERE email=? AND password=?", data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is", e)
        return False
    
def view():
    try:
        cursor.execute("SELECT * FROM Authen")
        return cursor.fetchall()
    except Exception as e:
        print("Errro is",e)
        return False
    
def single_user(id):
    try:
        cursor.execute("SELECT * FROM Authen WHERE id=?",(id,))
        return cursor.fetchone()
    except Exception as e :
        print("Error is",e)

def update(data):
    try:
        cursor.execute("UPDATE Authen SET username= ?, email= ?, password=? WHERE id=?", data)
        connection.commit()
        return True
    except Exception as e :
        print("Error is ",e)
        return False
    
def delete(id):
    try :
        cursor.execute("DELETE FROM Authen WHERE id=?", (id,))
        connection.commit()
        return True
    except Exception as e :
        print("Exception as",e)