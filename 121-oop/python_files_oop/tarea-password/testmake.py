import string
import random

def makePassword():
        return (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)))

pass1 = makePassword()
print(pass1)