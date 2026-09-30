# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 30/09/2026
# Purpose: 
# Usage: ./lab3a.py

import random as r
sequence=r.sample(range(0,100),20)
print("The sequence of 20 random numbers:", sequence)
sequence.sort()
print("The sequences sorted:", sequence)