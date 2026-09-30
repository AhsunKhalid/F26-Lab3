# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 30/09/2026
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

mylist =[]
while len(mylist)<6:
    num=int(input("Please enter a number:"))
    print ("You have entered:", num)
    num=num*10
    mylist.append(num)
# or mylist.append(num*10)
print(mylist)
print(mylist[::-1])
