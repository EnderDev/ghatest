import sys
import random

print("checking...")

rand = random.randint(0, 1)

if rand == 1:
    print("patches applied successfully")
else:
    sys.exit('!!! patches failed to apply !!!')