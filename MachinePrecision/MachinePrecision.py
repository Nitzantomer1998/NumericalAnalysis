# Author: Nitzan Tomer.
# Machine Precision.


# Variables
ourEpsilon = 1
loopsNum = 0

# "Function" To Find Your Machine Precision
print("\n[Machine Precision Find]")
while 1.0 + (ourEpsilon / 2) > 1.0:
    print(f'({loopsNum}) {ourEpsilon} \\ 2 = {ourEpsilon / 2}')
    loopsNum = loopsNum + 1
    ourEpsilon = ourEpsilon / 2

# Your Own Machine Precision
print(f'Your Epsilon Is --> {ourEpsilon}\n')
