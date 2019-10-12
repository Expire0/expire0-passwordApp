#!/usr/bin/env python3

from modules import config,classm


print("""
      Expire0 Pytool .Select a option below
      1. login lookup
      2. Insert new entry 
      3. Delete a entry
      4. Backup data to a sql file 
      5. Modify a entry
     """)

selection = input("Select a menu option:")
selection1 = int(selection)

if selection1 <= 5:
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

else:
    print("Please select a valid option")
