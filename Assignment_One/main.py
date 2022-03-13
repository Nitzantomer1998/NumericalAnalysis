# Author : Nitzan Tomer.
# Assignment Number One

# Question Two --> Machine Precision Find
# Question Two Variables
ourEpsilon = 0
arbitraryNum = 1
loopsNum = 0
flag = True

# Question Two Function
print("[Question Two]")
while flag:
    print(f'({loopsNum}) {arbitraryNum} \ 2 = {arbitraryNum / 2}')
    loopsNum = loopsNum + 1
    ourEpsilon = arbitraryNum
    arbitraryNum = arbitraryNum / 2
    if arbitraryNum == 0:
        flag = False
# Question Two Answer --> Your Own Machine Precision
print(f'Your Epsilon Is --> {ourEpsilon}\n')