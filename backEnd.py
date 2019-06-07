import sqlite3

def connect():
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY,user text,pword text)")
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,book text,author text,genre text)")
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,student text,pwords text)")
    conn.commit()
    conn.close()
def register(user,pword):
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO login VALUES (NULL,?,?)",(user,pword))
    conn.commit()
    conn.close()
def registerBook(book,author,genre):
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",(book,author,genre))
    conn.commit()
    conn.close()
def selectBook():
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    answer=cur.fetchall()
    return answer
def selectStudent():
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    answer=cur.fetchall()
    return answer
def search(name,passw):
    #print(name)
    #print(passw)
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM login")
    answer=cur.fetchone()
    print(answer)
    row=cur.execute("SELECT * FROM login WHERE user=? and pword=?",(name,passw)).fetchall()
    if not row:
        conn.close()
        return False
    else:
        conn.close()
        return True
def searchStudent(name,passw):
    conn = sqlite3.connect('creds.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.execute("SELECT * FROM student WHERE student=? and pwords=?", (name, passw)).fetchall()
    if not row:
        conn.close()
        return False
    else:
        conn.close()
        return True
def registerStudent(user,pword):
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?)",(user,pword))
    conn.commit()
    conn.close()
def deleteStudent(name):
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM student WHERE student=?",(name,))
    conn.commit()
    conn.close()

