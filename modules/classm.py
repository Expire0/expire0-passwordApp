#!/usr/bin/env python3



from pysqlcipher3 import dbapi2 as sqlcipher
#import sqlite3 as lite
from modules import config
from subprocess import Popen,PIPE
# import popen helper
import shlex 

def exconnect():
   
    vpy = input("Search for ?:" )
    clean = str(vpy)

    query = "select * from login where vendor like '%{}%' COLLATE NOCASE".format(clean)
    # Create a connection to the database
    con = sqlcipher.connect('db/encrypted.db')
  
    get_key = input("secret:")
    cur = con.cursor() 
    cur.execute('pragma key="{}"'.format(get_key))
    cur.execute(query)
    # Fetch the result of the query
    data = cur.fetchall()

    for i in data:
        print(i)

def inconnect():
    vendor = input("Please enter the vendor name: ") 
    login = input("Please enter the username: ")
    password = input("Please enter the password: ")
    website = input("Please enter the website address: ")
    comments = input("Please enter some comments: ")
    
    data = (vendor , login , password , website ,comments)
    data0 = "insert into login (vendor,Login,Pwd,Website,Comments) values {0}".format(data)

    #db connection 
    con = sqlcipher.connect('db/encrypted.db')
    cur = con.cursor()
    get_key = input("secret:")
    
    cur.execute('pragma key="{}"'.format(get_key))
    cur.execute(data0)
    con.commit()
    con.close()
    print("Data has been saved")


def delconnect():

    id0 =input("Please enter the id number:")
    data0 = "delete from login where ID = {}".format(id0)

    #db connection 
    con = sqlcipher.connect('db/encrypted.db')
    cur = con.cursor()
    get_key = input("secret:")
    
    cur.execute('pragma key="{}"'.format(get_key))
    cur.execute(data0)
    con.commit()
    con.close()
    print("Data has been removed")

def mod():
    password = input("Please enter the password: ")
    id0 =input("Please enter the id number:")
    data0 = "update login set Pwd={} where ID = {}".format(password,id0)

    #db connection 
    con = sqlcipher.connect('db/encrypted.db')
    cur = con.cursor()
    get_key = input("secret:")

    cur.execute('pragma key="{}"'.format(get_key))
    cur.execute(data0)
    con.commit()
    con.close()
    print("Data has been updated")



def backup():
    #use commit 
    #subprocess.call("mysqldump -u root  -D pytool > dumpfilename1.sql" , shell=True)
    comm = "cat /etc/os-release"
    arg = shlex.split(comm)
    complete = Popen(arg, stdout=PIPE , stderr=PIPE)

    try:
        outs , err = complete.communicate(timeout=5)
        return outs.decode("utf-8")
    except TimeoutExpired:
        complete.kill()
        outs, err = complete.communicate
        return err.decode("utf-8")

    




