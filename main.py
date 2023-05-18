import pymysql as a
try:# database connection
    con=a.connect(host='localhost',user='root',password='',database='cab')
    c=con.cursor()
    print('database connection done sucessfully')
except:
    print("can't established connection with database")

def reg():# Admin Registration Program
    try:
        d_name=input('Enter A Name:-')
        d_pas=input('Enter A Password:-')
        d_mail=input('Enter A Mail:-')
        d_phone=input('Enter A Phone Number:-')
        sql="insert into dealers (d_name,d_pas,d_mail,d_phone) values (%s,%s,%s,%s)"
        dealer=(d_name,d_pas,d_mail,d_phone)
        c.execute(sql,dealer)
        con.commit()
        con.close()
        print("New Dealer Added Sucessfully")
    except:
        print("Dealer Already Exists")
def login():# Admin Login
    try:
        con=a.connect(host='localhost',user='root',password='',database='cab') # Connect Updated DB
        c=con.cursor()
        d_name=input("Enter A Dealership Name:-")
        d_pas=input("Enter A Password :-")
        c.execute("select * from dealers where d_name=%s and d_pas=%s",[d_name,d_pas])
        if c.fetchone()==None:
            print(" **Wrong Dealership Name Or Password** ")
        else:
            print("""login sucessfully!!
            Now You Can Add , view , Update And Delete Your Cabs""")
            ch=1
            while ch!=0:
                ch=int(input("""\n
                        Press 1 For Add A New Cab .
                        Press 2 For veiw All your Cabs .
                        Press 3 For Update Any Information About Cab .
                        press 4 For Delete A Cab From Your List .
                        press 0 For Log Out .
                        Enter Your choice = """))
                if ch==0:# Logout
                    print("Thank You.Have a Nice Day")
                    pass
                elif ch==1: # Add New Cab
                    c_name=input("Enter Cab Name :- ")
                    c_type=input("Enter A Cab type :- ")
                    c_model=input("Enter A Cab Model :-")
                    d_id=None
                    did=c.execute("select d_id from dealers where d_name=%s and d_pas=%s",[d_name,d_pas])
                    gd=c.fetchall()
                    for did in gd:
                        d_id=did
                    c_from=input("Enter A Pick Up Place :- ")
                    c_to=input("Enter A Destination Place :-")
                    sql="insert into cabs (c_name,c_type,c_model,d_id,c_from,c_to) values (%s,%s,%s,%s,%s,%s)"
                    cabb=(c_name,c_type,c_model,d_id,c_from,c_to)
                    c.execute(sql,cabb)
                    con.commit()
                    con.close()
                    print("New Cab Add Sucessfully")    
                elif ch==2: # Show only Logged In Admin's cab Data
                    con=a.connect(host='localhost',user='root',password='',database='cab') # Connect Updated DB
                    c=con.cursor()
                    did=c.execute("select d_id from dealers where d_name=%s and d_pas=%s",[d_name,d_pas])
                    gd=c.fetchall()
                    for did in gd:
                        d_id=did
                    sc=c.execute("select * from cabs where d_id='%s'",d_id)
                    vc=c.fetchall()
                    for sc in vc:
                        print(sc)
                elif ch==3: # Update A Cab information
                    con=a.connect(host='localhost',user='root',password='',database='cab') # Connect Updated DB
                    c=con.cursor()
                    #print all recoard 
                    did=c.execute("select d_id from dealers where d_name=%s and d_pas=%s",[d_name,d_pas])
                    gd=c.fetchall()
                    for did in gd:
                        d_id=did
                    sc=c.execute("select * from cabs where d_id='%s'",d_id)
                    vc=c.fetchall()
                    for sc in vc:
                        print(sc)
                    #print recoard which will update
                    upid=int(input("Enter A Cab Id For Change Or Update Information : "))
                    sql=("select * from cabs where c_id='%s'",upid)
                    sq=c.fetchall()
                    for sql in sq:
                        print(sql)
                    #take updated data from Admin
                    print("Write In Place Of Corrections And Write The Rest As Is")
                    upname=input("Enter A Cab Name : ")
                    uptype=input("Enter A Cab Type : ")
                    upmodel=input("Enter A Cab Model : ")
                    upfrom=input("Enter A Cab Pick-up Place : ")
                    upto=input("Enter A Cab Destination : ")
                    # query for update record and execution
                    sql1=("update cabs set c_name=%s,c_type=%s,c_model=%s,c_from=%s,c_to=%s WHERE c_id='%s';")
                    rup=(upname,uptype,upmodel,upfrom,upto,upid)
                    c.execute(sql1,rup)
                    con.commit()
                    con.close()
                    print("Cab Information is Sucessfully Updated")
                elif ch==4: # delete a cab information
                    con=a.connect(host='localhost',user='root',password='',database='cab') # Connect Updated DB
                    c=con.cursor()
                    #print all recoard 
                    did=c.execute("select d_id from dealers where d_name=%s and d_pas=%s",[d_name,d_pas])
                    gd=c.fetchall()
                    for did in gd:
                        d_id=did
                    sc=c.execute("select * from cabs where d_id='%s'",d_id)
                    vc=c.fetchall()
                    for sc in vc:
                        print(sc)
                    d_id=int(input(" Enter A Cab Id for Delete Cab : "))
                    # Query of delete cab
                    c.execute("delete from cabs where c_id='%s'",d_id)
                    con.commit()
                    con.close()
                    print("Cab Is Deleted Sucessfully")
                else:
                    print("Enter A Valid Input")
    except:
        print(' **Something Went Wrong** ')
def u_reg():
    try:
        u_name=input('Enter A Name:-')
        u_pas=input('Enter A Password:-')
        u_mail=input('Enter A Mail:-')
        u_phone=input('Enter A Phone Number:-')
        sql="insert into user (u_name,u_pas,u_mail,u_phone) values (%s,%s,%s,%s)"
        user=(u_name,u_pas,u_mail,u_phone)
        c.execute(sql,user)
        con.commit()
        con.close()
        print("New User Added Sucessfully")
    except:
        print("User Already Exists")
def u_log():
    try:
        con=a.connect(host='localhost',user='root',password='',database='cab') # Connect Updated DB
        c=con.cursor()
        u_name=input("Enter A User Name:-")
        u_pas=input("Enter A Password :-")
        c.execute("select * from user where u_name=%s and u_pas=%s",[u_name,u_pas])
        if c.fetchone()==None:
            print(" **Wrong User Name Or Password** ")
        else:
            print("Login Sucessfully!!")
            con=a.connect(host='localhost',user='root',password='',database='cab') # Connect Updated DB
            c=con.cursor()
            ch=1
            while ch!=0:
                print("""
            Press 1 For Show Present Cab : 
            Press 2 For Change Profile : 
            Press 0 For Logout""")
                ch=int(input("Enter A Choice:"))
                if ch==1:# show cabs
                    sc=c.execute("select * from cabs")
                    vc=c.fetchall()
                    for sc in vc:
                        print(sc)
                elif ch==2:# update user information
                    u_id=None
                    upid=c.execute("select u_id from user where u_name=%s and u_pas=%s",[u_name,u_pas])
                    gd=c.fetchall()
                    for upid in gd:
                        u_id=upid 
                    print("Write In Place Of Corrections And Write The Rest As Is")
                    upname=input("Enter A User Name : ")
                    uppas=input("Enter A User Pass : ")
                    upmail=input("Enter A User mail : ")
                    upphone=input("Enter A User Phone : ")
                    u_id=int(u_id[0])
                    # query for update record and execution
                    sql1=("update user set u_name=%s,u_pas=%s,u_mail=%s,u_phone=%s where u_id='%s'")
                    upu=(upname,uppas,upmail,upphone,u_id)
                    c.execute(sql1,upu)
                    con.commit()
                    con.close() 
                    print("User Information is Sucessfully Updated")
                    
    except:
        print("**Something Went Wrong**")
# Main
b=1
while b!=0:
    b=int(input("""\n 
    Press 1 For Admin Registration : 
    Press 2 For Admin Login :
    Press 3 For User Registration : 
    Press 4 For User Login : 
    Press 0 For Exit :
    Enter Your choice = """))
    if b==0:
        break
    elif b==1:# Regitration 
        reg()
    elif b==2:# Login And Working Of Cab
        login()
    elif b==3:# user registration
        u_reg()
    elif b==4:# user login and update
        u_log()
