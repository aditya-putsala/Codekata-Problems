## Given a number N, print the product of the digits.
## Input Size : N <= 100000000000
## Sample Testcase :
## INPUT
## 2143
## OUTPUT
## 24

n = input()
sum = 1
for i in n:
    sum = sum * int(i)
print(sum)
