#!/usr/bin/env python3

### coding_by ay abdullahhi_333
### this code is work to tell you how  you can generate four name####


import random 
import string


def genaerate():
    n1 = random.choice(string.ascii_lowercase)
    n2 = random.choice(string.ascii_lowercase)
    n4 = random.choice(string.ascii_lowercase)
    n3 = random.choice(string.ascii_lowercase)
    name = n1+n2+n3+n4

    return name
print(genaerate())