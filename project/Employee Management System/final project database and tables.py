def database():
    import mysql.connector 
    mydb=mysql.connector.connect(host='localhost',user='root',password='soumil123')
    cur= mydb.cursor()
    cur.execute('CREATE DATABASE Employee_____management')
    print('Database Created')
def tables():
    import mysql.connector 
    mydb=mysql.connector.connect(host='localhost',user='root',password='soumil123',database='Employee_____management')
    cur= mydb.cursor()
    s= """CREATE TABLE office(Ecode int(20) primary key,Name VARCHAR(30) not null,Post VARCHAR(20),Joining VARCHAR(30),BASICPAY int,Status varchar(10) not null)"""
    cur.execute(s)

    v="""CREATE TABLE personal(Ecode int(20) primary key,name varchar(20) not null,city VARCHAR(30),Birthdate VARCHAR(20), phone VARCHAR(15),Status varchar(10) not null)"""
    cur.execute(v)
    print('tables created')
database()
tables()
