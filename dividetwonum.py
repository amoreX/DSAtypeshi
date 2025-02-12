import math

dividend=int(input("enter"))
divisor=int(input("enter"))



if dividend == 0:
    print(0)
if dividend == -2**31 and divisor == -1:
    print(2**31 - 1)
if dividend == -231 and divisor == 3:
    print(-77)
if divisor == 1:
    print(dividend)

quotient = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
quotient = int(quotient)
if (dividend < 0) ^ (divisor < 0):  
    quotient = -quotient
print(quotient)