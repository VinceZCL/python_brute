from string import *
from itertools import product
import sys
# import time

# initial = time.time()

characters=""

for c in sys.argv[1]:
    if c in ascii_uppercase:
        if ascii_uppercase in characters:
            pass
        else:
            characters += ascii_uppercase
    elif c in ascii_lowercase:
        if ascii_lowercase in characters:
            pass
        else:
            characters += ascii_lowercase
    elif c in digits:
        if digits in characters:
            pass
        else:
            characters += digits
    elif c in punctuation:
        if punctuation in characters:
            pass
        else:
            characters += punctuation

for pw in product(characters, repeat=len(sys.argv[1])):
    if pw == tuple([i for i in (sys.argv[1])]):
        print(*pw)
        # final = time.time()
        break
    else:
        print(*pw, end="\r")
        continue

# print(str(final-initial) + " second(s)")
