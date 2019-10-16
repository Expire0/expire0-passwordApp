#!/usr/bin/env python3

#from modules import config,classm
from modules import password
from sys import argv

script, pwdlen = argv


def genpwd():
    newpass = password.generate_pass(int(pwdlen))
    print(f"Your new password is: {newpass}")

print("""
      Expire0 Pytool. Select an option below:
      1. Login lookup
      2. Insert new entry 
      3. Delete an entry
      4. Backup data to a SQL file 
      5. Modify an entry
      6. Generate a random password
      7. Exit
     """)

selection = input("Select a menu option: ")
selection1 = int(selection)

if selection1 <= 7:
    if selection1 == 1:
        classm.exconnect()
    if selection1 == 2:
        classm.inconnect()
    if selection1 == 3:
        classm.delconnect()
    if selection1 == 4:
        print(classm.backup())
    if selection1 == 5:
        classm.mod()
    if selection1 == 6:
        genpwd()    
    if selection1 == 7:
        exit()

else:
    print("Please select a valid option:")


