#!/usr/bin/env python3

#from modules import config,classm
from modules import password
from sys import argv

script, pwdlen = argv

newpass = password.generate_pass(int(pwdlen))
print(f"Your new password is {newpass}")

print("""
      Expire0 Pytool .Select a option below:
      1. Login lookup
      2. Insert new entry 
      3. Delete a entry
      4. Backup data to a sql file 
      5. Modify a entry
      6. Exit
     """)

selection = input("Select a menu option: ")
selection1 = int(selection)

if selection1 <= 6:
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
        exit()

else:
    print("Please select a valid option")
