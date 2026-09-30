# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 30/09/2026
# Purpose: 
# Usage: ./lab3b.py

# Follow the specific instructions given in the README.md file

import random as r
sequence=r.sample(range(0,100),20)
print("The sequence of 20 random numbers:", sequence)
sequence.reverse()
print("The sequences reversed:", sequence)
#or you can do print(sequence[::-1])