import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='soumil123',database='Employee_____Management')
def npersonal():
    ans='y'or'Y'
    while ans=='y' or 'Y':
        n=int(input('Enter employee code: '))
        b=input('enter employee Name')
        c=input("Enter Employee's City Name:  ")
        d=input("Enter Employee's D.O.B: ")
        p=input("Enter Employee Phone: ")
        q=input('Enter Employee Status Active or not Active')
        data=(n,b,c,d,p,q)
        val='insert into personal values(%s,%s,%s,%s,%s,%s)'
        cur= mydb.cursor()
        cur.execute(val,data)
        mydb.commit()
        ans=input('To add more records press y else press n : ')
        if ans=='y':
            continue
        else:
            break
def personal():
   cur=mydb.cursor()
   cur.execute('select * from personal')
   rec=cur.fetchall()
   count=cur.rowcount
   print("+----------|--------------|-------------------------------------------------+")
   print("+  E code |   E Name      |    City  |  DOB:| phone:|  Status ")
   print("+----------|--------------|--------------------------------------------------+")
   for i in rec:
       print(i)
       print("+----------|--------------|----------------------------+")
   print("+   Total no. of records are : ",count,"    |")
   print("+------------------------------------------------------+")
def noffice():
    ans='y'or'Y'
    while ans=='y' or 'Y':
        ec=input('Enter Employee Code :')
        n=input('Enter Employee Name : ')
        ps=input("Enter Employee's Post :")
        j=input("Enter Employee's joininj date : ")
        bp=int(input('Enter Assigned Salary :'))
        s=input('Input Employee Status Active or Inactive')
        data=(ec,n,ps,j,bp,s)
        sql='insert into office values(%s,%s,%s,%s,%s,%s)'
        cur=mydb.cursor()
        cur.execute(sql,data)
        mydb.commit()
        print('Data Entered Successfully')
        ans=input('TO add more records pls enter Y else enter n')
        if ans=='y' or ans=='Y':
            continue
        else:
            break
def office():
    cur=mydb.cursor()
    cur.execute('select * from office')
    rec=cur.fetchall()
    count=cur.rowcount
    print("+----------|--------------|--------------------------------+")
    print("+  Ecode  |   Emp Name   |   Designation |  DOJ |  Salary :")
    print("+----------|--------------|--------------------------------+")
    for i in rec:
        print(i) 
        print("+----------|--------------|----------------------------+")
    print("+   Total no. of records are : ",count,"    |")
    print("+------------------------------------------------------+")
    
def search_record():
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1. Search Personal Details of Employee")
    print("2. Search Official Details of Employee")
    print()
    choice=int(input("ENTER THE CHOICE (1-2) : "))
    if choice==1:
          d=int(input("Enter Ecode of the employee which you want to search : "))
          query1="select * from personal where Ecode=%s" %(d)
    elif choice==2:
          Ecode=int(input("Enter Ecode which you want to search : "))
          query1="select * from office where Ecode='%s'" %(Ecode)
    
    else:
          print("Wrong Choice")
    cur=mydb.cursor()
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    
def delete_record():
    print('select any 1 option')
    print('1. delete Official records')
    print('2. delete personal records')
    ch=int(input('enter your Choice'))
    if ch==1:
        cur=mydb.cursor()
        d=int(input("Enter Ecode for deleting record : "))
        query1="delete from office where Ecode={0}".format(d)
        cur.execute(query1)
        mydb.commit()
        print("Record Deleted")
    elif ch==2:
        cur=mydb.cursor()
        e=int(input("Enter Ecode for deleting record : "))
        query2="delete from personal where Ecode={0}".format(e)
        cur.execute(query2)
        mydb.commit()
        print("Record Deleted")
    else:
        print('wrong choice')

    
def update():
    print('select any one of the following choices')
    print('1. update personal records')
    print('2. update official records')
    x=int(input('enter any one choice either 1 or 2'))
    if x==1:
        d=int(input("Enter Employee ID for update record : "))
        e=input("ENTER NEW City : ")
        f=input("ENTER NEW phone number  : ")
        query1="update personal set city='%s', phone='%s' where Ecode=%d ;" %(e,f,d)
        cur=mydb.cursor()
        cur.execute(query1)
        mydb.commit()
        print("Record Updated")
    elif x==2:
        d=int(input('Enter Employee Id for update record :'))
        e=input('enter the new designation')
        f=int(input('Enter new Salary'))
        query1=" update office set post='%s',basicpay=%d where Ecode=%d ;"%(e,f,d)
        cur=mydb.cursor()
        cur.execute(query1)
        mydb.commit()
        print('record updated')
    else:
        print('wrong choice')
def Employee_Exit():
    x=int(input('Enter ECode'))
    y='Inactive'
    cur=mydb.cursor()
    query1=" update office set Status='%s' where Ecode=%d;"%(y,x)
    query2= " update  personal set Status='%s' where Ecode=%d;"%(y,x)
    cur.execute(query1)
    cur.execute(query2)
    mydb.commit()
    print('Employee Exit Sucessful')
    

def main():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print("........MENU.......")
        print("1. Show personal details of all The existing Employee")
        print("2. SHOW official details of all the existing Employee")
        print("3. Enter Personal Details of a new Employee")
        print("4. Enter Official Details of a new Employee")
        print("5. Seacrh Records")
        print("6. Delete records")
        print("7. Update Records")
        print('8. Employee Exit ')
        print()
        choice=int(input("Enter the choice (1-6) : "))
        if(choice==1):
            personal()
        elif(choice==2):
            office()
        elif(choice==3):
            npersonal()
        elif(choice==4):
            noffice()
        elif(choice==5):
            search_record()
        elif(choice==6):
            delete_record()
        elif(choice==7):
            update()
        elif(choice==8):
            Employee_Exit()
        else:
            print("Wrong Choice.")
        loop=input("Do you want more try? Press 'y' to continue... or press'N' to exit")
        if loop=='y'or'Y':
            continue
        else:
            break
L=[]
main()
        

