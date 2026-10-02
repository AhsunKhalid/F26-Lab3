# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 30/09/2026
# Purpose: 
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

elements5=matrix[1][1] #Output:6
print("The element at second row and second coloum is ",elements5)
elements2=matrix[0][1] #Output:6
print("The element at first row and second coloum is ",elements2)
elements9=matrix[2][2] #Output:6
print("The element at third row and third coloum is ",elements9)

for i in matrix:
    print (i)