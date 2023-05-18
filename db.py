import pymysql as a
try:
    con=a.connect(host='localhost',user='root',password='',database='cab')
    c=con.cursor()
    print('done')
except:
    print('no')

# sql="create database cabs"
# c.execute(sql)


sql2="create table dealers (d_id int primary key auto_increment,d_name varchar(20) not null,d_pas varchar(20) unique not null,d_mail varchar(20) unique not null,d_phone varchar(10) unique not null)"
c.execute(sql2)
# s1="insert into dealers (d_name,d_pas,d_mail,d_phone) values ('temp','temp','temp','temp')"
sql3="create table user (u_id int primary key auto_increment,u_name varchar(20) not null,u_pas varchar(20) unique not null,u_mail varchar(20) unique not null,u_phone varchar(10) unique not null)"
c.execute(sql3)
sql4="create table cabs (c_id int primary key auto_increment,c_name varchar(20) not null,c_type varchar(20) not null,c_model varchar(20) not null,d_id int,FOREIGN KEY (d_id) REFERENCES dealers(d_id),c_from varchar(20) not null,c_to varchar(20) not null)"
c.execute(sql4)
con.commit()
